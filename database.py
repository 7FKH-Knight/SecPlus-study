import sqlite3
import json
import os

DB_PATH = os.environ.get("DB_PATH") or os.path.join(os.path.dirname(__file__), "study.db")


def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db


def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            domain INTEGER NOT NULL,
            subdomain TEXT NOT NULL,
            objective TEXT NOT NULL,
            stem TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            explanation_correct TEXT NOT NULL,
            explanation_a TEXT NOT NULL,
            explanation_b TEXT NOT NULL,
            explanation_c TEXT NOT NULL,
            explanation_d TEXT NOT NULL,
            difficulty INTEGER NOT NULL DEFAULT 3
        );
        CREATE TABLE IF NOT EXISTS sm2_cards (
            question_id INTEGER PRIMARY KEY REFERENCES questions(id),
            easiness REAL NOT NULL DEFAULT 2.5,
            interval INTEGER NOT NULL DEFAULT 0,
            repetitions INTEGER NOT NULL DEFAULT 0,
            next_review TEXT NOT NULL DEFAULT '2000-01-01',
            times_seen INTEGER NOT NULL DEFAULT 0,
            times_correct INTEGER NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS exam_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT NOT NULL,
            completed_at TEXT,
            mode TEXT NOT NULL,
            time_limit_sec INTEGER NOT NULL DEFAULT 5400,
            time_used_sec INTEGER,
            raw_score INTEGER,
            scaled_score INTEGER,
            passed INTEGER
        );
        CREATE TABLE IF NOT EXISTS exam_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL REFERENCES exam_sessions(id),
            question_id INTEGER NOT NULL REFERENCES questions(id),
            selected_answer TEXT,
            is_correct INTEGER NOT NULL DEFAULT 0,
            answered_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS drill_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL REFERENCES exam_sessions(id),
            question_id INTEGER NOT NULL REFERENCES questions(id),
            position INTEGER NOT NULL,
            answered INTEGER NOT NULL DEFAULT 0
        );
    """)
    db.commit()

    # Safe migrations — add columns only if they don't exist yet
    existing = {row[1] for row in db.execute("PRAGMA table_info(exam_sessions)").fetchall()}
    if "paused_at" not in existing:
        db.execute("ALTER TABLE exam_sessions ADD COLUMN paused_at TEXT")
    if "saved_answers" not in existing:
        db.execute("ALTER TABLE exam_sessions ADD COLUMN saved_answers TEXT")
    db.commit()
    db.close()


def load_questions(questions_path):
    db = get_db()
    count = db.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    if count > 0:
        db.close()
        return count

    with open(questions_path) as f:
        data = json.load(f)

    for q in data["questions"]:
        opts = q["options"]
        expl = q["explanations"]
        db.execute(
            """INSERT INTO questions
               (id, domain, subdomain, objective, stem,
                option_a, option_b, option_c, option_d,
                correct_answer,
                explanation_correct,
                explanation_a, explanation_b, explanation_c, explanation_d,
                difficulty)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                q["id"], q["domain"], q["subdomain"], q["objective"], q["stem"],
                opts["A"], opts["B"], opts["C"], opts["D"],
                q["correct_answer"],
                expl["correct"],
                expl["A"], expl["B"], expl["C"], expl["D"],
                q.get("difficulty", 3),
            ),
        )
        db.execute(
            "INSERT OR IGNORE INTO sm2_cards (question_id) VALUES (?)", (q["id"],)
        )

    db.commit()
    loaded = db.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    db.close()
    return loaded


def fetchone(sql, params=()):
    db = get_db()
    row = db.execute(sql, params).fetchone()
    db.close()
    return dict(row) if row else None


def fetchall(sql, params=()):
    db = get_db()
    rows = db.execute(sql, params).fetchall()
    db.close()
    return [dict(r) for r in rows]


def execute(sql, params=()):
    db = get_db()
    cur = db.execute(sql, params)
    db.commit()
    last_id = cur.lastrowid
    db.close()
    return last_id


def executemany(sql, param_list):
    db = get_db()
    db.executemany(sql, param_list)
    db.commit()
    db.close()
