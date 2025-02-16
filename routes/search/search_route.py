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

    if query:
        search_query = f"%{query}%"
        doodles = db.execute(
            "SELECT * FROM doodles WHERE title || ' ' || description LIKE ? ORDER BY created_at DESC",
            (search_query,),
        ).fetchall()
    else:
        doodles = []

    return render_template("search.html", doodles=doodles, query=query)
