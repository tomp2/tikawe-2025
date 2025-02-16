from datetime import datetime

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

doodle_blueprint = Blueprint("doodle", __name__, url_prefix="/doodle")


@doodle_blueprint.route("/<int:doodle_id>")
def page(doodle_id):
    db = get_db()
    db.execute("UPDATE doodles SET views = views + 1 WHERE id = ?", (doodle_id,))
    db.commit()
    doodle = db.execute("SELECT * FROM doodles WHERE id = ?", (doodle_id,)).fetchone()
    comments = db.execute(
        "SELECT comments.*, users.username FROM comments JOIN users ON comments.user_id = users.id WHERE doodle_id = ?",
        (doodle_id,),
    ).fetchall()

    reactions = db.execute(
        "SELECT emoji, COUNT(*) as count FROM reactions WHERE doodle_id = ? GROUP BY emoji",
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

    return render_template(
        "doodle.html",
        doodle=doodle,
        comments=comments,
        reactions=decoded_reactions,
        user_reactions=decoded_users_reactions,
    )


@doodle_blueprint.route("/<int:doodle_id>/react", methods=["POST"])
def toggle_reaction(doodle_id):
    if "user_id" not in session:
        flash("You must be logged in to react.", "error")
        return redirect(url_for("doodle.page", doodle_id=doodle_id))

    emoji_character = request.form["emoji"]

    db = get_db()
    existing_reaction_row = db.execute(
        "SELECT * FROM reactions WHERE doodle_id = ? AND user_id = ? AND emoji = ?",
        (doodle_id, session["user_id"], emoji_character),
    ).fetchone()

    if existing_reaction_row:
        db.execute(
            "DELETE FROM reactions WHERE doodle_id = ? AND user_id = ? AND emoji = ?",
            (doodle_id, session["user_id"], emoji_character),
        )
    else:
        db.execute(
            "INSERT INTO reactions (doodle_id, user_id, emoji, created_at) VALUES (?, ?, ?, ?)",
            (
                doodle_id,
                session["user_id"],
                emoji_character,
                datetime.utcnow().isoformat(),
            ),
        )

    all_doodle_reactions = db.execute(
        "SELECT COUNT(*) as count, emoji FROM reactions WHERE doodle_id = ? GROUP BY emoji",
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


@doodle_blueprint.route("/<int:doodle_id>/delete", methods=["POST"])
def delete_doodle(doodle_id):
    if "user_id" not in session:
        return {"error": "Unauthorized"}, 401

    user_id = session["user_id"]
    db = get_db()
    doodle = db.execute("SELECT * FROM doodles WHERE id = ?", (doodle_id,)).fetchone()

    if not doodle or doodle["user_id"] != user_id:
        return {"error": "Forbidden"}, 403

    db.execute("DELETE FROM doodles WHERE id = ?", (doodle_id,))
    db.commit()

    return redirect(url_for("profile.page"))


@doodle_blueprint.route("/<int:doodle_id>/comment", methods=["POST"])
def add_comment(doodle_id):
    if "user_id" not in session:
        return {"error": "Unauthorized"}, 401

    user_id = session["user_id"]
    content = request.json.get("content")

    if not content or len(content) > 500:
        return {"error": "Invalid comment"}, 400

    db = get_db()
    db.execute(
        "INSERT INTO comments (doodle_id, user_id, content, created_at) VALUES (?, ?, ?, ?)",
        (doodle_id, user_id, content, datetime.utcnow().isoformat()),
    )
    db.commit()

    return {"success": True}, 200


@doodle_blueprint.route(
    "/<int:doodle_id>/comment/<int:comment_id>/delete", methods=["POST"]
)
def delete_comment(doodle_id, comment_id):
    if "user_id" not in session:
        return {"error": "Unauthorized"}, 401

    user_id = session["user_id"]
    db = get_db()
    comment = db.execute(
        "SELECT * FROM comments WHERE id = ?", (comment_id,)
    ).fetchone()

    if not comment or comment["user_id"] != user_id:
        return {"error": "Forbidden"}, 403

    db.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
    db.commit()

    return {"success": True}, 200
