from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, jsonify, session, abort, g
from flask_login import login_required, current_user
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime, timedelta, timezone
import os
import random
import json
import secrets
import database as db
import sm2
from scoring import scale_score, domain_breakdown, select_exam_questions, DOMAIN_NAMES
from config import config
from auth import auth_bp, login_manager
from extensions import limiter

app = Flask(__name__)
env = os.environ.get("FLASK_ENV", "development")
app.config.from_object(config[env])

# Trust Railway's reverse proxy so rate limiting sees real client IPs
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

# Ensure DB tables exist regardless of whether started via gunicorn or directly
db.init_db()

# ── Auth ──────────────────────────────────────────────────────────────────────
login_manager.init_app(app)
login_manager.login_view = "auth.login"
app.register_blueprint(auth_bp)

# ── Rate limiting ─────────────────────────────────────────────────────────────
limiter.init_app(app)

# ── CSRF helper ───────────────────────────────────────────────────────────────
def generate_csrf():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(32)
    return session["csrf_token"]

app.jinja_env.globals["csrf_token"] = generate_csrf
app.jinja_env.globals["DOMAIN_NAMES"] = DOMAIN_NAMES


# ── Helpers ───────────────────────────────────────────────────────────────────

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


def owns_session(session_row):
    """Return True if current_user owns this DB session row."""
    uid = session_row.get("user_id")
    return uid is not None and uid == current_user.id


# ── Middleware ────────────────────────────────────────────────────────────────

@app.before_request
def set_csp_nonce():
    g.csp_nonce = secrets.token_hex(16)


app.jinja_env.globals["csp_nonce"] = lambda: getattr(g, "csp_nonce", "")


@app.before_request
def check_csrf():
    if request.method in ("POST", "PUT", "DELETE", "PATCH"):
        if request.is_json:
            token = request.headers.get("X-CSRF-Token", "")
        else:
            token = request.form.get("csrf_token", "")
        expected = session.get("csrf_token", "")
        if not expected or not secrets.compare_digest(token, expected):
            # Allow /login and /register (pre-session forms)
            if request.endpoint not in ("auth.login", "auth.register"):
                abort(403)


@app.after_request
def add_security_headers(response):
    nonce = getattr(g, "csp_nonce", "")
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = (
        f"default-src 'self'; script-src 'self' 'nonce-{nonce}'; "
        "style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
        "connect-src 'self'; font-src 'self'; object-src 'none'; base-uri 'self';"
    )
    response.headers["Permissions-Policy"] = (
        "geolocation=(), microphone=(), camera=(), payment=(), usb=()"
    )
    # M3: Always send HSTS in production — Railway proxy makes is_secure False
    if not app.config.get("DEBUG"):
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response


# ── Error handlers ────────────────────────────────────────────────────────────

@app.errorhandler(403)
def forbidden(_e):
    return render_template("error.html", code=403, msg="Access denied."), 403


@app.errorhandler(404)
def not_found(_e):
    return render_template("error.html", code=404, msg="Page not found."), 404


@app.errorhandler(429)
def rate_limited(_e):
    return render_template("error.html", code=429, msg="Too many requests. Please slow down."), 429


@app.errorhandler(500)
def server_error(_e):
    return render_template("error.html", code=500, msg="Something went wrong on our end."), 500


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
@login_required
def dashboard():
    uid = current_user.id
    stats = {}

    total_row = db.fetchone(
        "SELECT COUNT(*) as cnt, SUM(ea.is_correct) as correct "
        "FROM exam_answers ea JOIN exam_sessions es ON ea.session_id=es.id "
        "WHERE es.user_id=?", (uid,)
    )
    stats["total_answered"] = total_row["cnt"] or 0
    stats["total_correct"] = int(total_row["correct"] or 0)
    stats["overall_pct"] = (
        round(stats["total_correct"] / stats["total_answered"] * 100, 1)
        if stats["total_answered"] else 0
    )

    last3 = db.fetchall(
        "SELECT scaled_score FROM exam_sessions "
        "WHERE user_id=? AND mode='full_exam' AND scaled_score IS NOT NULL "
        "ORDER BY id DESC LIMIT 3", (uid,)
    )
    stats["est_score"] = (
        round(sum(r["scaled_score"] for r in last3) / len(last3)) if last3 else None
    )

    due_row = db.fetchone(
        "SELECT COUNT(*) as cnt FROM sm2_cards WHERE user_id=? AND next_review <= ?", (uid, today_str())
    )
    stats["cards_due"] = due_row["cnt"]

    domain_stats = []
    for d in range(1, 6):
        row = db.fetchone(
            "SELECT COUNT(*) as total, SUM(ea.is_correct) as correct "
            "FROM exam_answers ea "
            "JOIN questions q ON ea.question_id=q.id "
            "JOIN exam_sessions es ON ea.session_id=es.id "
            "WHERE q.domain=? AND es.user_id=?", (d, uid)
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

    streak = 0
    check_date = datetime.utcnow().date()
    while True:
        ds = check_date.strftime("%Y-%m-%d")
        row = db.fetchone(
            "SELECT COUNT(*) as cnt FROM exam_answers ea "
            "JOIN exam_sessions es ON ea.session_id=es.id "
            "WHERE date(ea.answered_at)=? AND es.user_id=?", (ds, uid)
        )
        if row["cnt"] > 0:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            break
    stats["streak"] = streak

    recent_sessions = db.fetchall(
        "SELECT id, started_at, scaled_score, passed, mode FROM exam_sessions "
        "WHERE user_id=? AND completed_at IS NOT NULL ORDER BY id DESC LIMIT 5", (uid,)
    )

    paused_sessions = db.fetchall(
        "SELECT id, started_at, mode, time_limit_sec, time_used_sec FROM exam_sessions "
        "WHERE user_id=? AND completed_at IS NULL AND paused_at IS NOT NULL "
        "ORDER BY paused_at DESC", (uid,)
    )

    sm2_dist = db.fetchall(
        "SELECT CASE "
        "WHEN interval=0 THEN 'new' "
        "WHEN interval BETWEEN 1 AND 6 THEN '1-6d' "
        "WHEN interval BETWEEN 7 AND 30 THEN '7-30d' "
        "ELSE '30d+' END as bucket, COUNT(*) as cnt "
        "FROM sm2_cards WHERE user_id=? GROUP BY bucket",
        (uid,)
    )
    sm2_buckets = {r["bucket"]: r["cnt"] for r in sm2_dist}

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_sessions=recent_sessions,
        paused_sessions=paused_sessions,
        sm2_buckets=sm2_buckets,
        now=datetime.now(timezone.utc),
    )


@app.route("/init")
def init():
    token = request.args.get("token") or ""
    expected = app.config.get("INIT_TOKEN") or ""
    if not expected or not secrets.compare_digest(token, expected):
        return "Forbidden", 403
    qpath = os.path.join(os.path.dirname(__file__), "questions.json")
    count = db.load_questions(qpath)
    return f"<h2>Loaded {count} questions, created {count} SM-2 cards.</h2><a href='/'>Go to dashboard</a>"


@app.route("/.well-known/assetlinks.json")
def assetlinks():
    """Required for Google Play TWA verification."""
    package = os.environ.get("ANDROID_PACKAGE", "com.yourname.secplusstudy")
    fingerprint = os.environ.get("ANDROID_FINGERPRINT", "")
    data = [{
        "relation": ["delegate_permission/common.handle_all_urls"],
        "target": {
            "namespace": "android_app",
            "package_name": package,
            "sha256_cert_fingerprints": [fingerprint] if fingerprint else [],
        },
    }]
    return jsonify(data)


@app.route("/exam/start")
@login_required
def exam_start():
    all_ids = get_all_ids_by_domain()
    question_ids = select_exam_questions(all_ids, total=90)

    session_id = db.execute(
        "INSERT INTO exam_sessions (user_id, started_at, mode, time_limit_sec) VALUES (?,?,?,?)",
        (current_user.id, now_str(), "full_exam", 5400),
    )

    rows = [(session_id, qid, pos) for pos, qid in enumerate(question_ids)]
    db.executemany(
        "INSERT INTO drill_queue (session_id, question_id, position) VALUES (?,?,?)", rows
    )

    return redirect(url_for("exam_view", session_id=session_id))


@app.route("/exam/<int:session_id>")
@login_required
def exam_view(session_id):
    sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not sess or not owns_session(sess):
        abort(403)

    time_remaining = sess["time_limit_sec"]
    if sess.get("time_used_sec"):
        time_remaining = max(0, sess["time_limit_sec"] - sess["time_used_sec"])

    saved_answers = {}
    if sess.get("saved_answers"):
        try:
            saved_answers = json.loads(sess["saved_answers"])
        except (ValueError, TypeError):
            saved_answers = {}

    q_rows = db.fetchall(
        "SELECT q.* FROM questions q "
        "JOIN drill_queue dq ON q.id=dq.question_id "
        "WHERE dq.session_id=? ORDER BY dq.position", (session_id,)
    )
    return render_template(
        "exam.html",
        session=sess,
        questions=q_rows,
        time_remaining=time_remaining,
        saved_answers=saved_answers,
    )


@app.route("/exam/<int:session_id>/pause", methods=["POST"])
@login_required
@limiter.limit("30 per minute")
def exam_pause(session_id):
    sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not sess or not owns_session(sess) or sess.get("completed_at"):
        return jsonify({"error": "not found or already completed"}), 400

    data = request.get_json(silent=True) or {}
    answers = data.get("answers", {})
    remaining = data.get("remaining_sec")

    time_used = (
        max(0, min(sess["time_limit_sec"] - remaining, sess["time_limit_sec"]))
        if remaining is not None
        else sess.get("time_used_sec") or 0
    )

    db.execute(
        "UPDATE exam_sessions SET paused_at=?, saved_answers=?, time_used_sec=? WHERE id=?",
        (now_str(), json.dumps(answers), time_used, session_id),
    )
    return jsonify({"ok": True})


@app.route("/exam/<int:session_id>/submit", methods=["POST"])
@login_required
@limiter.limit("5 per minute")
def exam_submit(session_id):
    sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not sess or not owns_session(sess):
        abort(403)

    # Atomic double-submit guard: only proceed if we can set completed_at
    rows_affected = db.update(
        "UPDATE exam_sessions SET completed_at=? WHERE id=? AND completed_at IS NULL",
        (now_str(), session_id),
    )
    if rows_affected == 0:
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
        [(r["session_id"], r["question_id"], r["selected"], r["is_correct"], ts)
         for r in answers_data],
    )

    exam_uid = current_user.id
    for row in answers_data:
        db.execute(
            "INSERT OR IGNORE INTO sm2_cards (user_id, question_id) VALUES (?,?)",
            (exam_uid, row["question_id"]),
        )
        card = db.fetchone(
            "SELECT * FROM sm2_cards WHERE user_id=? AND question_id=?",
            (exam_uid, row["question_id"]),
        )
        if card:
            quality = sm2.quality_from_correct(row["is_correct"])
            new_e, new_i, new_r, next_rev = sm2.update_card(
                card["easiness"], card["interval"], card["repetitions"], quality
            )
            db.execute(
                "UPDATE sm2_cards SET easiness=?, interval=?, repetitions=?, next_review=?, "
                "times_seen=times_seen+1, times_correct=times_correct+? "
                "WHERE user_id=? AND question_id=?",
                (new_e, new_i, new_r, next_rev, row["is_correct"], exam_uid, row["question_id"]),
            )

    scaled = scale_score(raw_correct, len(q_rows))
    passed = 1 if scaled >= 750 else 0
    # Use the server-tracked value (updated by heartbeats every 30s); ignore client-submitted time
    time_used = max(0, min(sess.get("time_used_sec") or 0, sess["time_limit_sec"]))

    db.execute(
        "UPDATE exam_sessions SET raw_score=?, scaled_score=?, passed=?, "
        "time_used_sec=?, paused_at=NULL, saved_answers=NULL WHERE id=?",
        (raw_correct, scaled, passed, time_used, session_id),
    )

    return redirect(url_for("exam_results", session_id=session_id))


@app.route("/exam/<int:session_id>/results")
@login_required
def exam_results(session_id):
    sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not sess or not owns_session(sess):
        abort(403)

    answers = db.fetchall(
        "SELECT ea.*, q.domain FROM exam_answers ea JOIN questions q ON ea.question_id=q.id "
        "WHERE ea.session_id=?", (session_id,)
    )
    breakdown = domain_breakdown([dict(a) for a in answers])
    return render_template("exam_results.html", session=sess, breakdown=breakdown)


@app.route("/exam/<int:session_id>/review")
@login_required
def exam_review(session_id):
    sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not sess or not owns_session(sess):
        abort(403)

    rows = db.fetchall(
        "SELECT ea.selected_answer, ea.is_correct, q.* "
        "FROM exam_answers ea JOIN questions q ON ea.question_id=q.id "
        "WHERE ea.session_id=? ORDER BY q.domain, q.id", (session_id,)
    )
    return render_template("review.html", session_id=session_id, rows=rows)


@app.route("/drill/start")
@login_required
def drill_start():
    due = db.fetchall(
        "SELECT question_id FROM sm2_cards WHERE user_id=? AND next_review <= ? ORDER BY next_review LIMIT 30",
        (current_user.id, today_str())
    )
    due_ids = {r["question_id"] for r in due}

    uid = current_user.id
    weak_ids = set()
    for d in range(1, 6):
        row = db.fetchone(
            "SELECT COUNT(*) as total, SUM(ea.is_correct) as correct "
            "FROM exam_answers ea "
            "JOIN questions q ON ea.question_id=q.id "
            "JOIN exam_sessions es ON ea.session_id=es.id "
            "WHERE q.domain=? AND es.user_id=?", (d, uid)
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
        rows = db.fetchall("SELECT id FROM questions ORDER BY RANDOM() LIMIT 20")
        all_ids = [r["id"] for r in rows]

    random.shuffle(all_ids)
    all_ids = all_ids[:40]

    session_id = db.execute(
        "INSERT INTO exam_sessions (user_id, started_at, mode, time_limit_sec) VALUES (?,?,?,?)",
        (current_user.id, now_str(), "drill", 0),
    )

    rows = [(session_id, qid, pos) for pos, qid in enumerate(all_ids)]
    db.executemany(
        "INSERT INTO drill_queue (session_id, question_id, position) VALUES (?,?,?)", rows
    )

    return redirect(url_for("drill_question", session_id=session_id))


@app.route("/drill/<int:session_id>/question")
@login_required
def drill_question(session_id):
    sess = db.fetchone(
        "SELECT * FROM exam_sessions WHERE id=? AND mode='drill'", (session_id,)
    )
    if not sess or not owns_session(sess):
        abort(403)

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
        session=sess,
        question=next_q,
        answered=answered,
        total=total,
    )


@app.route("/drill/<int:session_id>/answer", methods=["POST"])
@login_required
@limiter.limit("120 per minute")
def drill_answer(session_id):
    sess = db.fetchone(
        "SELECT * FROM exam_sessions WHERE id=? AND mode='drill'", (session_id,)
    )
    if not sess or not owns_session(sess):
        return jsonify({"error": "forbidden"}), 403

    question_id = request.form.get("question_id", type=int)
    selected = request.form.get("selected_answer")

    if selected not in {"A", "B", "C", "D"}:
        return jsonify({"error": "invalid answer"}), 400

    # Verify this question belongs to the current drill session and isn't already answered
    dq = db.fetchone(
        "SELECT id FROM drill_queue WHERE session_id=? AND question_id=? AND answered=0",
        (session_id, question_id),
    )
    if not dq:
        return jsonify({"error": "invalid question for this session"}), 400

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

    drill_uid = current_user.id
    db.execute(
        "INSERT OR IGNORE INTO sm2_cards (user_id, question_id) VALUES (?,?)",
        (drill_uid, question_id),
    )
    card = db.fetchone(
        "SELECT * FROM sm2_cards WHERE user_id=? AND question_id=?",
        (drill_uid, question_id),
    )
    if card:
        quality = sm2.quality_from_correct(is_correct)
        new_e, new_i, new_r, next_rev = sm2.update_card(
            card["easiness"], card["interval"], card["repetitions"], quality
        )
        db.execute(
            "UPDATE sm2_cards SET easiness=?, interval=?, repetitions=?, next_review=?, "
            "times_seen=times_seen+1, times_correct=times_correct+? "
            "WHERE user_id=? AND question_id=?",
            (new_e, new_i, new_r, next_rev, is_correct, drill_uid, question_id),
        )

    return jsonify({
        "is_correct": bool(is_correct),
        "correct_answer": q["correct_answer"],
        "explanations": {
            "correct": q["explanation_correct"],
            "A": q["explanation_a"],
            "B": q["explanation_b"],
            "C": q["explanation_c"],
            "D": q["explanation_d"],
        },
        "explanation_correct": q["explanation_correct"],
    })


@app.route("/drill/<int:session_id>/results")
@login_required
def drill_results(session_id):
    sess = db.fetchone(
        "SELECT * FROM exam_sessions WHERE id=? AND mode='drill'", (session_id,)
    )
    if not sess or not owns_session(sess):
        abort(403)

    answers = db.fetchall(
        "SELECT ea.*, q.stem, q.domain FROM exam_answers ea "
        "JOIN questions q ON ea.question_id=q.id WHERE ea.session_id=?", (session_id,)
    )
    total = len(answers)
    correct = sum(1 for a in answers if a["is_correct"])
    return render_template(
        "drill_results.html",
        session=sess,
        answers=answers,
        total=total,
        correct=correct,
    )


@app.route("/history")
@login_required
def history():
    sessions = db.fetchall(
        "SELECT *, "
        "CASE WHEN completed_at IS NOT NULL THEN 'completed' "
        "     WHEN paused_at IS NOT NULL THEN 'paused' "
        "     ELSE 'in progress' END as status "
        "FROM exam_sessions WHERE user_id=? ORDER BY id DESC LIMIT 50",
        (current_user.id,)
    )
    return render_template("history.html", sessions=sessions)


@app.route("/history/<int:session_id>/delete", methods=["POST"])
@login_required
def history_delete(session_id):
    sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
    if not sess or not owns_session(sess):
        abort(403)
    db.execute("DELETE FROM exam_answers WHERE session_id=?", (session_id,))
    db.execute("DELETE FROM drill_queue WHERE session_id=?", (session_id,))
    db.execute("DELETE FROM exam_sessions WHERE id=?", (session_id,))
    return redirect(url_for("history"))


@app.route("/history/clear", methods=["POST"])
@login_required
def history_clear():
    uid = current_user.id
    completed = db.fetchall(
        "SELECT id FROM exam_sessions WHERE user_id=? AND completed_at IS NOT NULL", (uid,)
    )
    for s in completed:
        db.execute("DELETE FROM exam_answers WHERE session_id=?", (s["id"],))
        db.execute("DELETE FROM drill_queue WHERE session_id=?", (s["id"],))
    db.execute(
        "DELETE FROM exam_sessions WHERE user_id=? AND completed_at IS NOT NULL", (uid,)
    )
    return redirect(url_for("history"))


@app.route("/api/heartbeat", methods=["POST"])
@login_required
@limiter.limit("120 per minute")
def heartbeat():
    data = request.get_json(silent=True) or {}
    session_id = data.get("session_id")
    remaining = data.get("remaining_sec")
    if session_id and remaining is not None:
        sess = db.fetchone("SELECT * FROM exam_sessions WHERE id=?", (session_id,))
        if sess and owns_session(sess) and sess["time_limit_sec"] and not sess["completed_at"]:
            used = max(0, min(sess["time_limit_sec"] - remaining, sess["time_limit_sec"]))
            db.execute(
                "UPDATE exam_sessions SET time_used_sec=? WHERE id=?", (used, session_id)
            )
    return jsonify({"ok": True})


@app.route("/api/stats")
@login_required
def api_stats():
    uid = current_user.id
    row = db.fetchone(
        "SELECT COUNT(*) as total, SUM(ea.is_correct) as correct "
        "FROM exam_answers ea JOIN exam_sessions es ON ea.session_id=es.id "
        "WHERE es.user_id=?", (uid,)
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
