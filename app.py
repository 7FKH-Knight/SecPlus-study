from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
import os
import random
import json
import database as db
import sm2
from scoring import scale_score, domain_breakdown, select_exam_questions, DOMAIN_NAMES
from config import config

app = Flask(__name__)
env = os.environ.get("FLASK_ENV", "development")
app.config.from_object(config[env])


# ── helpers ──────────────────────────────────────────────────────────────────

def now_str():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")


def today_str():
    return datetime.utcnow().strftime("%Y-%m-%d")


def get_all_ids_by_domain():
    rows = db.fetchall("SELECT id, domain FROM questions")
    result = {}
    for r in rows:
        result.setdefault(r["domain"], []).append(r["id"])
    return result


# ── CSRF protection ────────────────────────────────────────────────────────────

@app.before_request
def check_csrf():
    if request.method in ("POST", "PUT", "DELETE", "PATCH"):
        if request.is_json:
            return
        origin = request.headers.get("Origin") or request.headers.get("Referer", "")
        if request.host not in origin:
            return "Forbidden", 403


# ── routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def dashboard():
    stats = {}

    total_row = db.fetchone(
        "SELECT COUNT(*) as cnt, SUM(is_correct) as correct FROM exam_answers"
    )
    stats["total_answered"] = total_row["cnt"] or 0
    stats["total_correct"] = int(total_row["correct"] or 0)
    stats["overall_pct"] = (
        round(stats["total_correct"] / stats["total_answered"] * 100, 1)
        if stats["total_answered"] else 0
    )

    last3 = db.fetchall(
        "SELECT scaled_score FROM exam_sessions WHERE mode='full_exam' AND scaled_score IS NOT NULL ORDER BY id DESC LIMIT 3"
    )
    if last3:
        stats["est_score"] = round(sum(r["scaled_score"] for r in last3) / len(last3))
    else:
        stats["est_score"] = None

    due_row = db.fetchone(
        "SELECT COUNT(*) as cnt FROM sm2_cards WHERE next_review <= ?", (today_str(),)
    )
    stats["cards_due"] = due_row["cnt"]

    domain_stats = []
    for d in range(1, 6):
        row = db.fetchone(
            "SELECT COUNT(*) as total, SUM(is_correct) as correct FROM exam_answers ea "
            "JOIN questions q ON ea.question_id=q.id WHERE q.domain=?", (d,)
        )
        total = row["total"] or 0
        correct = int(row["correct"] or 0)
        pct = round(correct / total * 100, 1) if total else 0
        domain_stats.append({
            "domain": d,
            "name": DOMAIN_NAMES[d],
            "correct": correct,
            "total": total,
            "pct": pct,
            "weak": pct < 70 and total > 0,
        })
    stats["domains"] = domain_stats

    # Study streak
    streak = 0
    check_date = datetime.utcnow().date()
    while True:
        ds = check_date.strftime("%Y-%m-%d")
        row = db.fetchone(
            "SELECT COUNT(*) as cnt FROM exam_answers WHERE date(answered_at)=?", (ds,)
        )
        if row["cnt"] > 0:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break
    stats["streak"] = streak

    recent_sessions = db.fetchall(
        "SELECT id, started_at, scaled_score, passed, mode FROM exam_sessions "
        "WHERE completed_at IS NOT NULL ORDER BY id DESC LIMIT 5"
    )

    paused_sessions = db.fetchall(
        "SELECT id, started_at, mode, time_limit_sec, time_used_sec FROM exam_sessions "
        "WHERE completed_at IS NULL AND paused_at IS NOT NULL ORDER BY paused_at DESC"
    )

    sm2_dist = db.fetchall(
        "SELECT CASE "
        "WHEN interval=0 THEN 'new' "
        "WHEN interval BETWEEN 1 AND 6 THEN '1-6d' "
        "WHEN interval BETWEEN 7 AND 30 THEN '7-30d' "
        "ELSE '30d+' END as bucket, COUNT(*) as cnt "
        "FROM sm2_cards GROUP BY bucket"
    )
    sm2_buckets = {r["bucket"]: r["cnt"] for r in sm2_dist}

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_sessions=recent_sessions,
        paused_sessions=paused_sessions,
        sm2_buckets=sm2_buckets,
    )


@app.route("/init")
def init():
    token = request.args.get("token")
    expected = app.config.get("INIT_TOKEN")
    if not expected or token != expected:
        return "Forbidden", 403
    qpath = os.path.join(os.path.dirname(__file__), "questions.json")
    count = db.load_questions(qpath)
    return f"<h2>Loaded {count} questions, created {count} SM-2 cards.</h2><a href='/'>Go to dashboard</a>"


@app.route("/exam/start")
def exam_start():
    all_ids = get_all_ids_by_domain()
    question_ids = select_exam_questions(all_ids, total=90)

    session_id = db.execute(
        "INSERT INTO exam_sessions (started_at, mode, time_limit_sec) VALUES (?,?,?)",
        (now_str(), "full_exam", 5400),
    )

    rows = [(session_id, qid, pos) for pos, qid in enumerate(question_ids)]
    db.executemany(
        "INSERT INTO drill_queue (session_id, question_id, position) VALUES (?,?,?)", rows
    )

    return redirect(url_for("exam_view", session_id=session_id))


@app.route("/exam/<int:session_id>")
def exam_view(session_id):
    session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not session:
        return "Session not found", 404

    # Calculate remaining time (accounts for time already used in a previous sitting)
    time_remaining = session["time_limit_sec"]
    if session.get("time_used_sec"):
        time_remaining = max(0, session["time_limit_sec"] - session["time_used_sec"])

    saved_answers = {}
    if session.get("saved_answers"):
        try:
            saved_answers = json.loads(session["saved_answers"])
        except (ValueError, TypeError):
            saved_answers = {}

    q_rows = db.fetchall(
        "SELECT q.* FROM questions q "
        "JOIN drill_queue dq ON q.id=dq.question_id "
        "WHERE dq.session_id=? ORDER BY dq.position", (session_id,)
    )
    return render_template(
        "exam.html",
        session=session,
        questions=q_rows,
        time_remaining=time_remaining,
        saved_answers=saved_answers,
    )


@app.route("/exam/<int:session_id>/pause", methods=["POST"])
def exam_pause(session_id):
    session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not session or session.get("completed_at"):
        return jsonify({"error": "not found or already completed"}), 400

    data = request.get_json(silent=True) or {}
    answers = data.get("answers", {})
    remaining = data.get("remaining_sec")

    time_used = (
        session["time_limit_sec"] - remaining
        if remaining is not None
        else session.get("time_used_sec") or 0
    )

    db.execute(
        "UPDATE exam_sessions SET paused_at=?, saved_answers=?, time_used_sec=? WHERE id=?",
        (now_str(), json.dumps(answers), time_used, session_id),
    )
    return jsonify({"ok": True})


@app.route("/exam/<int:session_id>/submit", methods=["POST"])
def exam_submit(session_id):
    session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not session:
        return "Session not found", 404

    # Guard against double-submit (page reload would corrupt SM-2 cards)
    if session.get("completed_at"):
        return redirect(url_for("exam_results", session_id=session_id))

    q_rows = db.fetchall(
        "SELECT q.* FROM questions q "
        "JOIN drill_queue dq ON q.id=dq.question_id "
        "WHERE dq.session_id=? ORDER BY dq.position", (session_id,)
    )

    answers_data = []
    raw_correct = 0
    for q in q_rows:
        selected = request.form.get(f"q_{q['id']}")
        if selected not in {"A", "B", "C", "D", None}:
            selected = None
        is_correct = 1 if selected == q["correct_answer"] else 0
        raw_correct += is_correct
        answers_data.append({
            "session_id": session_id,
            "question_id": q["id"],
            "selected": selected,
            "is_correct": is_correct,
        })

    ts = now_str()
    db.executemany(
        "INSERT INTO exam_answers (session_id, question_id, selected_answer, is_correct, answered_at) "
        "VALUES (?,?,?,?,?)",
        [(row["session_id"], row["question_id"], row["selected"], row["is_correct"], ts)
         for row in answers_data],
    )

    # Update SM-2 cards
    for row in answers_data:
        card = db.fetchone("SELECT * FROM sm2_cards WHERE question_id=?", (row["question_id"],))
        if card:
            quality = sm2.quality_from_correct(row["is_correct"])
            new_e, new_i, new_r, next_rev = sm2.update_card(
                card["easiness"], card["interval"], card["repetitions"], quality
            )
            db.execute(
                "UPDATE sm2_cards SET easiness=?, interval=?, repetitions=?, next_review=?, "
                "times_seen=times_seen+1, times_correct=times_correct+? WHERE question_id=?",
                (new_e, new_i, new_r, next_rev, row["is_correct"], row["question_id"]),
            )

    scaled = scale_score(raw_correct, len(q_rows))
    passed = 1 if scaled >= 750 else 0
    time_used = request.form.get("time_used_sec", type=int)

    db.execute(
        "UPDATE exam_sessions SET completed_at=?, raw_score=?, scaled_score=?, passed=?, time_used_sec=? WHERE id=?",
        (now_str(), raw_correct, scaled, passed, time_used, session_id),
    )

    return redirect(url_for("exam_results", session_id=session_id))


@app.route("/exam/<int:session_id>/results")
def exam_results(session_id):
    session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not session:
        return "Session not found", 404

    answers = db.fetchall(
        "SELECT ea.*, q.domain FROM exam_answers ea JOIN questions q ON ea.question_id=q.id "
        "WHERE ea.session_id=?", (session_id,)
    )
    breakdown = domain_breakdown([dict(a) for a in answers])

    return render_template("exam_results.html", session=session, breakdown=breakdown)


@app.route("/exam/<int:session_id>/review")
def exam_review(session_id):
    rows = db.fetchall(
        "SELECT ea.selected_answer, ea.is_correct, q.* "
        "FROM exam_answers ea JOIN questions q ON ea.question_id=q.id "
        "WHERE ea.session_id=? ORDER BY q.domain, q.id", (session_id,)
    )
    return render_template("review.html", session_id=session_id, rows=rows)


@app.route("/drill/start")
def drill_start():
    # Build queue: SM-2 due cards + weak domain cards
    due = db.fetchall(
        "SELECT question_id FROM sm2_cards WHERE next_review <= ? ORDER BY next_review LIMIT 30",
        (today_str(),)
    )
    due_ids = {r["question_id"] for r in due}

    # Add weak-domain questions (< 70% accuracy)
    weak_ids = set()
    for d in range(1, 6):
        row = db.fetchone(
            "SELECT COUNT(*) as total, SUM(is_correct) as correct FROM exam_answers ea "
            "JOIN questions q ON ea.question_id=q.id WHERE q.domain=?", (d,)
        )
        total = row["total"] or 0
        correct = int(row["correct"] or 0)
        if total == 0 or (correct / total) < 0.70:
            domain_qs = db.fetchall(
                "SELECT id FROM questions WHERE domain=? ORDER BY RANDOM() LIMIT 10", (d,)
            )
            weak_ids.update(r["id"] for r in domain_qs)

    all_ids = list(due_ids | weak_ids)
    if not all_ids:
        # Cold start — random sample
        rows = db.fetchall("SELECT id FROM questions ORDER BY RANDOM() LIMIT 20")
        all_ids = [r["id"] for r in rows]

    random.shuffle(all_ids)
    all_ids = all_ids[:40]

    session_id = db.execute(
        "INSERT INTO exam_sessions (started_at, mode, time_limit_sec) VALUES (?,?,?)",
        (now_str(), "drill", 0),
    )

    rows = [(session_id, qid, pos) for pos, qid in enumerate(all_ids)]
    db.executemany(
        "INSERT INTO drill_queue (session_id, question_id, position) VALUES (?,?,?)", rows
    )

    return redirect(url_for("drill_question", session_id=session_id))


@app.route("/drill/<int:session_id>/question")
def drill_question(session_id):
    session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not session:
        return "Session not found", 404

    next_q = db.fetchone(
        "SELECT dq.id as dq_id, dq.position, q.* FROM drill_queue dq "
        "JOIN questions q ON dq.question_id=q.id "
        "WHERE dq.session_id=? AND dq.answered=0 ORDER BY dq.position LIMIT 1",
        (session_id,)
    )

    if not next_q:
        db.execute(
            "UPDATE exam_sessions SET completed_at=? WHERE id=?", (now_str(), session_id)
        )
        return redirect(url_for("drill_results", session_id=session_id))

    total = db.fetchone(
        "SELECT COUNT(*) as cnt FROM drill_queue WHERE session_id=?", (session_id,)
    )["cnt"]
    answered = db.fetchone(
        "SELECT COUNT(*) as cnt FROM drill_queue WHERE session_id=? AND answered=1", (session_id,)
    )["cnt"]

    return render_template(
        "drill.html",
        session=session,
        question=next_q,
        answered=answered,
        total=total,
    )


@app.route("/drill/<int:session_id>/answer", methods=["POST"])
def drill_answer(session_id):
    question_id = request.form.get("question_id", type=int)
    selected = request.form.get("selected_answer")

    if selected not in {"A", "B", "C", "D"}:
        return jsonify({"error": "invalid answer"}), 400

    q = db.fetchone("SELECT * FROM questions WHERE id=?", (question_id,))
    if not q:
        return jsonify({"error": "not found"}), 404

    is_correct = 1 if selected == q["correct_answer"] else 0

    db.execute(
        "INSERT INTO exam_answers (session_id, question_id, selected_answer, is_correct, answered_at) "
        "VALUES (?,?,?,?,?)",
        (session_id, question_id, selected, is_correct, now_str()),
    )

    db.execute(
        "UPDATE drill_queue SET answered=1 WHERE session_id=? AND question_id=?",
        (session_id, question_id),
    )

    card = db.fetchone("SELECT * FROM sm2_cards WHERE question_id=?", (question_id,))
    if card:
        quality = sm2.quality_from_correct(is_correct)
        new_e, new_i, new_r, next_rev = sm2.update_card(
            card["easiness"], card["interval"], card["repetitions"], quality
        )
        db.execute(
            "UPDATE sm2_cards SET easiness=?, interval=?, repetitions=?, next_review=?, "
            "times_seen=times_seen+1, times_correct=times_correct+? WHERE question_id=?",
            (new_e, new_i, new_r, next_rev, is_correct, question_id),
        )

    explanations = {
        "correct": q["explanation_correct"],
        "A": q["explanation_a"],
        "B": q["explanation_b"],
        "C": q["explanation_c"],
        "D": q["explanation_d"],
    }

    return jsonify({
        "is_correct": bool(is_correct),
        "correct_answer": q["correct_answer"],
        "explanations": explanations,
        "explanation_correct": q["explanation_correct"],
    })


@app.route("/drill/<int:session_id>/results")
def drill_results(session_id):
    session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    answers = db.fetchall(
        "SELECT ea.*, q.stem, q.domain FROM exam_answers ea JOIN questions q ON ea.question_id=q.id "
        "WHERE ea.session_id=?", (session_id,)
    )
    total = len(answers)
    correct = sum(1 for a in answers if a["is_correct"])
    return render_template(
        "drill_results.html",
        session=session,
        answers=answers,
        total=total,
        correct=correct,
    )


@app.route("/history")
def history():
    sessions = db.fetchall(
        "SELECT *, "
        "CASE WHEN completed_at IS NOT NULL THEN 'completed' "
        "     WHEN paused_at IS NOT NULL THEN 'paused' "
        "     ELSE 'in progress' END as status "
        "FROM exam_sessions ORDER BY id DESC LIMIT 30"
    )
    return render_template("history.html", sessions=sessions)


@app.route("/api/heartbeat", methods=["POST"])
def heartbeat():
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")
    remaining = data.get("remaining_sec")
    if session_id and remaining is not None:
        session = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
        if session and session["time_limit_sec"] and not session["completed_at"]:
            used = session["time_limit_sec"] - remaining
            db.execute(
                "UPDATE exam_sessions SET time_used_sec=? WHERE id=?", (used, session_id)
            )
    return jsonify({"ok": True})


@app.route("/api/stats")
def api_stats():
    row = db.fetchone(
        "SELECT COUNT(*) as total, SUM(is_correct) as correct FROM exam_answers"
    )
    cards_due = db.fetchone(
        "SELECT COUNT(*) as cnt FROM sm2_cards WHERE next_review <= ?", (today_str(),)
    )["cnt"]
    return jsonify({
        "total_answered": row["total"] or 0,
        "total_correct": int(row["correct"] or 0),
        "cards_due": cards_due,
    })


if __name__ == "__main__":
    db.init_db()
    app.run(
        debug=app.config["DEBUG"],
        port=int(os.environ.get("PORT", 5001)),
    )
