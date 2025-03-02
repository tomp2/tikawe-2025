import re
import secrets
import sqlite3

from flask import (
    request,
    redirect,
    url_for,
    session,
    Blueprint,
    render_template,
    flash,
)
from werkzeug.security import generate_password_hash

from database import get_db

register_blueprint = Blueprint("register", __name__, url_prefix="/register")


@register_blueprint.route("/", methods=["GET", "POST"])
def page():
    if "user_id" in session:
        flash("You are already logged in!", "error")
        return redirect(url_for("profile.page"))

    if request.method == "GET":
        return render_template("register.html")

    username = request.form["username"]
    if len(username) < 3:
        flash("Username must be at least 3 characters long!", "error")
        return redirect(url_for("register.page"))
    if len(username) > 16:
        flash("Username must be at most 16 characters long!", "error")
        return redirect(url_for("register.page"))
    if not re.match(r"^[a-zäöåA-ZÄÖÅ0-9_-]+$", username):
        flash("Username must only contain letters, numbers, dashes, and underscores!", "error")
        return redirect(url_for("register.page"))

    password = request.form["password"]
    if len(password) < 12:
        flash("Password must be at least 12 characters long!", "error")
        return redirect(url_for("register.page"))
    if len(password) > 128:
        flash("Password must be at most 64 characters long!", "error")
        return redirect(url_for("register.page"))
    if not re.match(r"^[a-zöäåA-ZÄÖÅ0-9!@#$%^&*()_+-=]+$", password):
        flash("Password must only contain letters, numbers and special characters (!@#$%^&*()_+-=)", "error")
        return redirect(url_for("register.page"))

    db = get_db()
    hashed_password = generate_password_hash(password)
    try:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, hashed_password),
        )
        db.commit()
        user = db.execute(
            "SELECT id FROM users WHERE username = ?", (username,)
        ).fetchone()
        session["user_id"] = user["id"]
        session["csrf_token"] = secrets.token_hex(16)
        return redirect(url_for("home.page"))
    except sqlite3.IntegrityError:
        flash("Username taken!", "error")
        return redirect(url_for("register.page"))
