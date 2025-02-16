from flask import (
    request,
    redirect,
    url_for,
    session,
    render_template,
    Blueprint,
)
from werkzeug.security import check_password_hash

from database import get_db


login_blueprint = Blueprint("login", __name__, url_prefix="/login")


@login_blueprint.route("/", methods=["GET", "POST"])
def page():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            return redirect(url_for("home.page"))
        return "Invalid credentials!"
    return render_template("login.html")
