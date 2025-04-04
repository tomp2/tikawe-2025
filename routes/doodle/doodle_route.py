from flask import (
    request,
    redirect,
    url_for,
    session,
    json,
    flash,
    Blueprint,
    render_template,
)

from database import get_db
from security_utils import check_csrf

doodle_blueprint = Blueprint("doodle", __name__, url_prefix="/doodle")


@doodle_blueprint.route("/<int:doodle_id>")
def page(doodle_id):
    db = get_db()
    doodle = db.execute("SELECT id, title, likes, image_url, user_id, description, views FROM doodles WHERE id = ?", (doodle_id,)).fetchone()
    if not doodle:
        return render_template("post_not_found.html"), 404

    db.execute("UPDATE doodles SET views = views + 1 WHERE id = ?", (doodle_id,))
    db.commit()

    comments = db.execute(
        "SELECT username, content, comments.id, username, user_id FROM comments JOIN users ON comments.user_id = users.id WHERE doodle_id = ?",
        (doodle_id,),
    ).fetchall()

    reactions = db.execute(
        "SELECT emoji, COUNT(1) as count FROM reactions WHERE doodle_id = ? GROUP BY emoji",
        (doodle_id,),
    ).fetchall()
    decoded_reactions = {reaction["emoji"]: reaction["count"] for reaction in reactions}

    decoded_users_reactions = {}
    if "user_id" in session:
        post_reactions = db.execute(
            "SELECT emoji FROM reactions WHERE doodle_id = ? AND user_id = ?",
            (doodle_id, session["user_id"]),
        ).fetchall()
        decoded_users_reactions = {reaction["emoji"] for reaction in post_reactions}

    user_like_row = db.execute(
        "SELECT id FROM likes WHERE doodle_id = ? AND user_id = ?",
        (doodle_id, session.get("user_id")),
    ).fetchone()

    doodle_tags = db.execute(
        "SELECT tag FROM doodle_tags WHERE doodle_id = ?", (doodle_id,)
    ).fetchall()

    return render_template(
        "doodle.html",
        doodle=doodle,
        comments=comments,
        reactions=decoded_reactions,
        user_reactions=decoded_users_reactions,
        user_has_liked=bool(user_like_row),
        doodle_tags=doodle_tags,
    )


@doodle_blueprint.route("/<int:doodle_id>/react", methods=["POST"])
def toggle_reaction(doodle_id):
    if "user_id" not in session:
        flash("You must be logged in to react.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    check_csrf()

    db = get_db()
    doodle = db.execute("SELECT user_id FROM doodles WHERE id = ?", (doodle_id,)).fetchone()

    if not doodle or doodle["user_id"] == session["user_id"]:
        flash("You cannot react to your own post.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    emoji_character = request.form["emoji"]
    existing_reaction_row = db.execute(
        "SELECT id FROM reactions WHERE doodle_id = ? AND user_id = ? AND emoji = ?",
        (doodle_id, session["user_id"], emoji_character),
    ).fetchone()

    if existing_reaction_row:
        db.execute(
            "DELETE FROM reactions WHERE doodle_id = ? AND user_id = ? AND emoji = ?",
            (doodle_id, session["user_id"], emoji_character),
        )
    else:
        db.execute(
            "INSERT INTO reactions (doodle_id, user_id, emoji) VALUES (?, ?, ?)",
            (doodle_id, session["user_id"], emoji_character),
        )

    all_doodle_reactions = db.execute(
        "SELECT COUNT(1) as count, emoji FROM reactions WHERE doodle_id = ? GROUP BY emoji",
        (doodle_id,),
    ).fetchall()
    encoded_doodle_row_reactions_json = json.dumps(
        {
            hex(ord(reaction["emoji"]))[2:]: reaction["count"]
            for reaction in all_doodle_reactions
        }
    )
    db.execute(
        "UPDATE doodles SET reactions = ? WHERE id = ?",
        (encoded_doodle_row_reactions_json, doodle_id),
    )

    db.commit()
    return redirect(url_for("doodle.page", doodle_id=doodle_id))


@doodle_blueprint.route("/<int:doodle_id>/like", methods=["POST"])
def toggle_like(doodle_id):
    if "user_id" not in session:
        flash("You must be logged in to add likes.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    check_csrf()

    db = get_db()
    doodle = db.execute("SELECT user_id FROM doodles WHERE id = ?", (doodle_id,)).fetchone()

    if not doodle or doodle["user_id"] == session["user_id"]:
        flash("You cannot like your own post.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    existing_like_row = db.execute(
        "SELECT id FROM likes WHERE doodle_id = ? AND user_id = ?",
        (doodle_id, session["user_id"]),
    ).fetchone()

    if existing_like_row:
        db.execute(
            "DELETE FROM likes WHERE doodle_id = ? AND user_id = ?",
            (doodle_id, session["user_id"]),
        )
        like_count_change = -1
    else:

        db.execute(
            "INSERT INTO likes (doodle_id, user_id) VALUES (?, ?)",
            (
                doodle_id,
                session["user_id"],
            ),
        )
        like_count_change = 1

    db.execute(
        "UPDATE doodles SET likes = likes + ? WHERE id = ?",
        (like_count_change, doodle_id),
    )
    db.commit()

    return redirect(url_for("doodle.page", doodle_id=doodle_id))


@doodle_blueprint.route("/<int:doodle_id>/delete", methods=["POST"])
def delete_doodle(doodle_id):
    if "user_id" not in session:
        return {"error": "Unauthorized"}, 401

    check_csrf()

    user_id = session["user_id"]
    db = get_db()
    doodle = db.execute("SELECT user_id FROM doodles WHERE id = ?", (doodle_id,)).fetchone()

    if not doodle or doodle["user_id"] != user_id:
        flash("You can only delete your own doodles.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    db.execute("DELETE FROM doodles WHERE id = ?", (doodle_id,))
    db.commit()

    return redirect(url_for("profile.page"))


@doodle_blueprint.route("/<int:doodle_id>/comment", methods=["POST"])
def add_comment(doodle_id):
    if "user_id" not in session:
        flash("You must be logged in to comment.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    check_csrf()

    user_id = session["user_id"]
    content = request.form["content"]

    if not content or len(content) > 150:
        return {"error": "Invalid comment"}, 400

    db = get_db()
    db.execute(
        "INSERT INTO comments (doodle_id, user_id, content) VALUES (?, ?, ?)",
        (doodle_id, user_id, content),
    )
    db.execute(
        "UPDATE doodles SET comments = comments + 1 WHERE id = ?",
        (doodle_id,),
    )
    db.commit()

    return redirect(url_for("doodle.page", doodle_id=doodle_id))


@doodle_blueprint.route(
    "/<int:doodle_id>/comment/<int:comment_id>/delete", methods=["POST"]
)
def delete_comment(doodle_id, comment_id):
    if "user_id" not in session:
        flash("You must be logged in to delete a comment.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    check_csrf()

    user_id = session["user_id"]
    db = get_db()
    comment = db.execute(
        "SELECT user_id FROM comments WHERE id = ?", (comment_id,)
    ).fetchone()

    if not comment or comment["user_id"] != user_id:
        flash("You can only delete your own comments.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    db.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
    db.execute(
        "UPDATE doodles SET comments = comments - 1 WHERE id = ?",
        (doodle_id,),
    )

    db.commit()

    return redirect(url_for("doodle.page", doodle_id=doodle_id))
