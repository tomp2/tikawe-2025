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


@register_blueprint.route("/", methods=["POST"])
def page():
    if "user_id" in session:
        flash("You are already logged in!", "error")
        return redirect(url_for("profile.page"))

    if request.method == "GET":
        return render_template("register.html")

    username = request.form["username"]
    password = request.form["password"]
    db = get_db()
    hashed_password = generate_password_hash(password)
    try:
        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, hashed_password),
        )
        db.commit()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        session["user_id"] = user["id"]
        session["csrf_token"] = secrets.token_hex(16)
        return redirect(url_for("home.page"))
    except sqlite3.IntegrityError:
        flash("Username taken!", "error")
        return redirect(url_for("register.page"))
