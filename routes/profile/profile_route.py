import json

from flask import Blueprint, render_template, session, redirect, url_for
from database import get_db

profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")


@profile_blueprint.route("/")
def page():
    if "user_id" not in session:
        return redirect(url_for("login.page"))

    db = get_db()
    user_id = session["user_id"]

    user_posts = db.execute(
        "SELECT * FROM doodles WHERE user_id = ? ORDER BY created_at DESC", (user_id,)
    ).fetchall()
    for doodle in user_posts:
        reactions = json.loads(doodle["reactions"])
        doodle["reactions"] = {
            chr(int(emoji, 16)): count for emoji, count in reactions.items()
        }

    liked_posts = db.execute(
        """
        SELECT d.* FROM doodles d
        JOIN likes l ON d.id = l.doodle_id
        WHERE l.user_id = ?
        ORDER BY l.created_at DESC
        """,
        (user_id,),
    ).fetchall()
    for doodle in liked_posts:
        reactions = json.loads(doodle["reactions"])
        doodle["reactions"] = {
            chr(int(emoji, 16)): count for emoji, count in reactions.items()
        }

    user_comments = db.execute(
        """
        SELECT c.content, c.created_at, d.title, d.id AS doodle_id
        FROM comments c
        JOIN doodles d ON c.doodle_id = d.id
        WHERE c.user_id = ?
        ORDER BY c.created_at DESC
        """,
        (user_id,),
    ).fetchall()

    return render_template(
        "profile.html",
        user_posts=user_posts,
        liked_posts=liked_posts,
        user_comments=user_comments,
    )
