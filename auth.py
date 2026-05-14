from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import database as db

auth_bp = Blueprint("auth", __name__)
login_manager = LoginManager()


class User(UserMixin):
    def __init__(self, row):
        self.id = row["id"]
        self.username = row["username"]
        self.email = row["email"]

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
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        if not username or len(username) < 3:
            error = "Username must be at least 3 characters."
        elif not email or "@" not in email:
            error = "Enter a valid email address."
        elif password != confirm:
            error = "Passwords do not match."
        else:
            error = _validate_password(password)

        if error is None:
            existing = db.fetchone(
                "SELECT id FROM users WHERE username=? OR email=?", (username, email)
            )
            if existing:
                error = "Username or email already taken."
            else:
                from datetime import datetime
                db.execute(
                    "INSERT INTO users (username, email, password_hash, created_at) VALUES (?,?,?,?)",
                    (username, email, generate_password_hash(password),
                     datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")),
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
        password = request.form.get("password", "")

        row = db.fetchone(
            "SELECT * FROM users WHERE username=? OR email=?",
            (identifier, identifier.lower()),
        )
        if row and check_password_hash(row["password_hash"], password):
            user = User(row)
            login_user(user, remember=bool(request.form.get("remember")))
            next_page = request.args.get("next")
            return redirect(next_page if next_page and next_page.startswith("/") else url_for("dashboard"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error, registered=registered)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
