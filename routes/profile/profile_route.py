from flask import (
    redirect,
    url_for,
    session,
    flash,
    Blueprint,
    render_template,
)

from database import get_db

profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")


@profile_blueprint.route("/")
def page():
    if "user_id" not in session:
        flash("You must be logged in to view your doodles.", "error")
        return redirect(url_for("login.page"))

    db = get_db()
    user_id = session["user_id"]
    doodles = db.execute(
        "SELECT * FROM doodles WHERE user_id = ? ORDER BY created_at DESC", (user_id,)
    ).fetchall()
    return render_template("home.html", doodles=doodles)
