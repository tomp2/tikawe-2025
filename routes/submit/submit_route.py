import uuid

from flask import (
    request,
    redirect,
    url_for,
    session,
    Blueprint,
    render_template,
)

from config import USER_IMAGE_UPLOADS_PATH
from database import get_db

submit_blueprint = Blueprint("submit", __name__, url_prefix="/submit")


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}


def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@submit_blueprint.route("/", methods=["GET"])
def page():
    if "user_id" not in session:
        return redirect(url_for("login.page"))
    return render_template("submit.html")


@submit_blueprint.route("/", methods=["POST"])
def submit():
    user_id = session.get("user_id")
    if user_id is None:
        return "Not logged in", 401

    if "image" not in request.files:
        return "No image uploaded", 400

    title = request.form["title"]
    if not title:
        return "Title is required", 400
    if len(title) > 40:
        return "Title is too long", 400
    if len(title) < 3:
        return "Title is too short", 400

    description = request.form["description"]
    if len(description) > 80:
        return "Description is too long", 400

    tags = request.form["tags"]
    if len(tags) > 40:
        return "Tags are too long", 400

    image = request.files["image"]
    if not image or not is_allowed_file(image.filename):
        return "Invalid file type", 400

    filename = f"{uuid.uuid4()}.png"
    safe_filename = USER_IMAGE_UPLOADS_PATH / filename

    image.save(safe_filename)

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO doodles (title, description, tags, image_url, user_id)
        VALUES (?, ?, ?, ?, ?)
    """,
        (title, description, tags, safe_filename.name, user_id),
    )
    conn.commit()

    return redirect("/")
