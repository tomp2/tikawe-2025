from flask import (
    request,
    Blueprint,
    render_template,
)

from database import get_db

search_blueprint = Blueprint("search", __name__, url_prefix="/search")


@search_blueprint.route("/", methods=["GET"])
def page():
    query = request.args.get("q", "").strip()
    db = get_db()

    doodles = []
    if query.startswith("#") and len(query) > 1:  # Tag search
        tag_name = query[1:]
        doodles = db.execute(
            """
            SELECT d.* FROM doodles d
            JOIN doodle_tags dt ON d.id = dt.doodle_id
            JOIN tags t ON dt.tag = t.name
            WHERE t.name = ?
            ORDER BY d.created_at DESC
            """,
            (tag_name,),
        ).fetchall()
    elif query:
        search_query = f"%{query}%"
        doodles = db.execute(
            "SELECT * FROM doodles WHERE title || ' ' || description LIKE ? ORDER BY created_at DESC",
            (search_query,),
        ).fetchall()

    return render_template("search.html", doodles=doodles, query=query)
