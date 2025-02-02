import sqlite3
from datetime import datetime
from pathlib import Path
import uuid
from flask import Flask, g, send_file, render_template, request, redirect, url_for, session, json
from werkzeug.security import generate_password_hash, check_password_hash

import config

app = Flask(__name__)
app.secret_key = config.secret_key
DATABASE = Path("data.db")
USER_IMAGE_UPLOADS = Path("user_image_uploads")

if not USER_IMAGE_UPLOADS.exists():
    USER_IMAGE_UPLOADS.mkdir()


@app.route("/")
def index():
    db = get_db()
    query = "SELECT * FROM doodles ORDER BY created_at DESC LIMIT 10"
    doodles = db.execute(query).fetchall()
    return render_template("home.html", doodles=doodles)


@app.route("/doodle/<int:doodle_id>")
def view_doodle(doodle_id):
    db = get_db()
    db.execute("UPDATE doodles SET views = views + 1 WHERE id = ?", (doodle_id,))
    db.commit()
    doodle = db.execute("SELECT * FROM doodles WHERE id = ?", (doodle_id,)).fetchone()
    comments = db.execute(
        "SELECT comments.*, users.username FROM comments JOIN users ON comments.user_id = users.id WHERE doodle_id = ?",
        (doodle_id,)
    ).fetchall()

    reactions = json.loads(doodle["reactions"])
    decoded_reactions = {chr(int(key, 16)): value for key, value in reactions.items()}
    return render_template("doodle.html", doodle=doodle, comments=comments, reactions=decoded_reactions)


@app.route("/submit", methods=["GET"])
def submit():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("submit.html")


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/submit', methods=['POST'])
def submit_doodle():
    user_id = session.get('user_id')
    if user_id is None:
        return 'Not logged in', 401

    if 'image' not in request.files:
        return 'No image uploaded', 400

    title = request.form['title']
    if not title:
        return 'Title is required', 400
    if len(title) > 40:
        return 'Title is too long', 400
    if len(title) < 3:
        return 'Title is too short', 400

    description = request.form['description']
    if len(description) > 80:
        return 'Description is too long', 400

    tags = request.form['tags']
    if len(tags) > 40:
        return 'Tags are too long', 400

    image = request.files['image']
    if not image or not is_allowed_file(image.filename):
        return 'Invalid file type', 400

    filename = f'{uuid.uuid4()}.png'
    safe_filename = USER_IMAGE_UPLOADS / filename

    image.save(safe_filename)

    created_at = datetime.utcnow().isoformat()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO doodles (title, description, tags, image_url, user_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, description, tags, safe_filename.name, user_id, created_at))
    conn.commit()

    return redirect('/')


@app.route("/doodle/<int:doodle_id>/delete", methods=["POST"])
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

    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        hashed_password = generate_password_hash(password)
        try:
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, hashed_password)
            )
            db.commit()
            user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        except sqlite3.IntegrityError:
            return "Username taken!"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        return "Invalid credentials!"
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route('/image/<filename>')
def serve_image(filename):
    if (safe_path := USER_IMAGE_UPLOADS / filename).exists():
        return send_file(safe_path)
    else:
        return 'File not found', 404


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

        def make_dicts(cursor, row):
            return dict((cursor.description[idx][0], value)
                        for idx, value in enumerate(row))

        db.row_factory = make_dicts

    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    print("Initializing database")
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        print("Database created")


if __name__ == '__main__':
    if not DATABASE.exists():
        init_db()
    app.run()
