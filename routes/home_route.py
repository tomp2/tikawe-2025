from flask import render_template, json, Blueprint, request

from database import get_db
from config import POSTS_PER_PAGE

home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.route("/")
def page():
    db = get_db()

    page = request.args.get("page", 1, int)
    offset = (page - 1) * POSTS_PER_PAGE

    query = """
        SELECT id, image_url, reactions, title, description, views, comments, likes, tags
        FROM doodles 
        ORDER BY created_at 
        DESC LIMIT ?
        OFFSET ?
    """
    doodles = db.execute(query, (POSTS_PER_PAGE, offset)).fetchall()
    doodles_with_decoded_reactions = []
    for doodle in doodles:
        reactions = json.loads(doodle["reactions"])
        decoded_reactions = {
            chr(int(emoji, 16)): count for emoji, count in reactions.items()
        }
        doodle["reactions"] = decoded_reactions
        doodles_with_decoded_reactions.append(doodle)

    total_posts = db.execute("SELECT COUNT(1) AS count FROM doodles").fetchone()
    total_pages = (total_posts["count"] + POSTS_PER_PAGE - 1) // POSTS_PER_PAGE

    return render_template(
        "home.html", doodles=doodles, total_pages=total_pages, page=page
    )
