import secrets

from flask import (
    request,
    redirect,
    url_for,
    session,
    render_template,
    Blueprint,
    flash,
)
from werkzeug.security import check_password_hash

from database import get_db


login_blueprint = Blueprint("login", __name__, url_prefix="/login")


@login_blueprint.route("/", methods=["GET", "POST"])
def page():
    if "user_id" in session:
        return redirect(url_for("profile.page"))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT id, password_hash FROM users WHERE username = ?", (username,)
        ).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["csrf_token"] = secrets.token_hex(16)
            return redirect(url_for("home.page"))

        flash("Incorrect username or password", "error")

    return render_template("login.html")
