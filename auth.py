import hashlib
import re
from datetime import datetime, timedelta

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import database as db

auth_bp = Blueprint("auth", __name__)
login_manager = LoginManager()


def hash_email(email):
    """One-way SHA-256 hash — raw emails are never stored."""
    return hashlib.sha256(email.lower().strip().encode()).hexdigest()


class User(UserMixin):
    def __init__(self, row):
        self.id = row["id"]
        self.username = row["username"]
        self.email = row["email"]   # stored as hash

    @staticmethod
    def get(user_id):
        row = db.fetchone("SELECT * FROM users WHERE id=?", (user_id,))
        return User(row) if row else None


@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))


def _validate_username(u):
    if len(u) < 3:
        return "Username must be at least 3 characters."
    if len(u) > 32:
        return "Username must be 32 characters or fewer."
    if not re.match(r"^[A-Za-z0-9_-]+$", u):
        return "Username may only contain letters, numbers, underscores, and hyphens."
    return None


def _validate_password(pw):
    if len(pw) < 8:
        return "Password must be at least 8 characters."
    if not any(c.isdigit() for c in pw):
        return "Password must contain at least one number."
    return None


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm", "")

        error = _validate_username(username)
        if error is None and ("@" not in email or "." not in email.split("@")[-1]):
            error = "Enter a valid email address."
        elif error is None and password != confirm:
            error = "Passwords do not match."
        elif error is None:
            error = _validate_password(password)

        if error is None:
            email_hash = hash_email(email)
            existing = db.fetchone(
                "SELECT id FROM users WHERE username=? OR email=?", (username, email_hash)
            )
            if existing:
                error = "Username or email already taken."
            else:
                db.execute(
                    "INSERT INTO users (username, email, password_hash, created_at) VALUES (?,?,?,?)",
                    (
                        username,
                        email_hash,
                        generate_password_hash(password, method="pbkdf2:sha256"),
                        datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
                    ),
                )
                return redirect(url_for("auth.login") + "?registered=1")

    return render_template("register.html", error=error)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    registered = request.args.get("registered")
    error = None

    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip()
        password   = request.form.get("password", "")

        # Look up by hashed email or by username
        if "@" in identifier:
            row = db.fetchone("SELECT * FROM users WHERE email=?", (hash_email(identifier),))
        else:
            row = db.fetchone("SELECT * FROM users WHERE username=?", (identifier,))

        if not row:
            error = "Invalid username or password."
        else:
            locked_until = row.get("locked_until")
            if locked_until and datetime.utcnow() < datetime.fromisoformat(locked_until):
                remaining = int(
                    (datetime.fromisoformat(locked_until) - datetime.utcnow()).total_seconds()
                )
                mins = max(1, remaining // 60)
                error = f"Account locked after too many failed attempts. Try again in {mins} minute(s)."
            elif check_password_hash(row["password_hash"], password):
                db.execute(
                    "UPDATE users SET failed_attempts=0, locked_until=NULL WHERE id=?",
                    (row["id"],),
                )
                login_user(User(row), remember=bool(request.form.get("remember")))
                next_page = request.args.get("next")
                return redirect(
                    next_page if next_page and next_page.startswith("/") else url_for("dashboard")
                )
            else:
                attempts = (row.get("failed_attempts") or 0) + 1
                new_locked = None
                if attempts >= 5:
                    new_locked = (datetime.utcnow() + timedelta(minutes=15)).strftime(
                        "%Y-%m-%dT%H:%M:%S"
                    )
                    attempts = 0
                    error = "Too many failed attempts. Account locked for 15 minutes."
                else:
                    error = "Invalid username or password."
                db.execute(
                    "UPDATE users SET failed_attempts=?, locked_until=? WHERE id=?",
                    (attempts, new_locked, row["id"]),
                )

    return render_template("login.html", error=error, registered=registered)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
