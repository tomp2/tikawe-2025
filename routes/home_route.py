from flask import render_template, json, Blueprint

from database import get_db


home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.route("/")
def page():
    db = get_db()
    query = "SELECT * FROM doodles ORDER BY created_at DESC LIMIT 10"
    doodles = db.execute(query).fetchall()
    doodles_with_decoded_reactions = []
    for doodle in doodles:
        reactions = json.loads(doodle["reactions"])
        decoded_reactions = {
            chr(int(emoji, 16)): count for emoji, count in reactions.items()
        }
        doodle["reactions"] = decoded_reactions
        doodles_with_decoded_reactions.append(doodle)
    return render_template("home.html", doodles=doodles)
