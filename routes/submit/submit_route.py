import uuid

from flask import (
    request,
    redirect,
    url_for,
    session,
    Blueprint,
    render_template,
    flash,
)

from config import USER_IMAGE_UPLOADS_PATH
from database import get_db
from security_utils import check_csrf

submit_blueprint = Blueprint("submit", __name__, url_prefix="/submit")


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}


def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@submit_blueprint.route("/", methods=["GET"])
def page():
    if "user_id" not in session:
        flash("You must be logged in to submit a doodle", "error")
        return redirect(url_for("login.page"))

    db = get_db()
    tags = db.execute("SELECT name FROM tags").fetchall()
    return render_template("submit.html", tags=tags)


@submit_blueprint.route("/", methods=["POST"])
def submit():
    user_id = session.get("user_id")
    if not user_id:
        flash("You must be logged in to submit a doodle", "error")
        return redirect(url_for("login.page"))

    check_csrf()

    if "image" not in request.files:
        flash("No file detected in submission", "error")
        return redirect(url_for("submit.page"))

    title = request.form["title"]
    if not title:
        flash("Title is required", "error")
        return redirect(url_for("submit.page"))
    if len(title) > 40:
        flash("Title is too long (max 40 characters)", "error")
        return redirect(url_for("submit.page"))
    if len(title) < 3:
        flash("Title is too short (min 3 characters)", "error")
        return redirect(url_for("submit.page"))

    description = request.form["description"]
    if len(description) > 80:
        flash("Description is too long (max 80 characters)", "error")
        return redirect(url_for("submit.page"))

    image = request.files.get("image")
    if not image or not is_allowed_file(image.filename):
        flash(
            f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}",
            "error",
        )
        return redirect(url_for("submit.page"))

    db = get_db()
    all_tag_rows = db.execute("SELECT name FROM tags").fetchall()
    all_tags = {tag["name"] for tag in all_tag_rows}

    tags = request.form.getlist("tags")
    if not tags:
        flash("At least one tag is required", "error")
        return redirect(url_for("submit.page"))
    for tag in tags:
        if tag not in all_tags:
            print(f"Invalid tag: {tag}")
            flash(f"Unknown tag: {tag}", "error")
            return redirect(url_for("submit.page"))
    tags_string = ",".join(tags)

    filename = f"{uuid.uuid4()}.png"
    safe_filename = USER_IMAGE_UPLOADS_PATH / filename

    image.save(safe_filename)

    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO doodles (title, description, image_url, user_id, tags)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, description, safe_filename.name, user_id, tags_string),
    )
    doodle_id = cursor.lastrowid

    inserts = [(doodle_id, tag) for tag in tags]
    cursor.executemany(
        "INSERT INTO doodle_tags (doodle_id, tag) VALUES (?, ?)", inserts
    )

    db.commit()
    return redirect("/")
