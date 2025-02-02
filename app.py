import sqlite3
from datetime import datetime
from pathlib import Path
import uuid
from flask import Flask, g, send_file, render_template, request, redirect, url_for, session, json, flash
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


@app.route("/profile")
def view_profile():
    if "user_id" not in session:
        flash("You must be logged in to view your doodles.", "error")
        return redirect(url_for("login"))

    db = get_db()
    user_id = session["user_id"]
    doodles = db.execute(
        "SELECT * FROM doodles WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    ).fetchall()
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

    reactions = db.execute(
        "SELECT emoji, COUNT(*) as count FROM reactions WHERE doodle_id = ? GROUP BY emoji",
        (doodle_id,)
    ).fetchall()

    decoded_reactions = {
        chr(int(reaction["emoji"], 16)): reaction["count"]
        for reaction in reactions
    }

    decoded_users_reactions = {}
    if "user_id" in session:
        post_reactions = db.execute(
            "SELECT emoji FROM reactions WHERE doodle_id = ? AND user_id = ?",
            (doodle_id, session["user_id"])
        ).fetchall()

        decoded_users_reactions = {chr(int(reaction["emoji"], 16)) for reaction in post_reactions}

    return render_template("doodle.html", doodle=doodle, comments=comments, reactions=decoded_reactions,
                           user_reactions=decoded_users_reactions)


@app.route("/search", methods=["GET"])
def search_doodles():
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


@app.route("/doodle/<int:doodle_id>/react", methods=["POST"])
def toggle_reaction(doodle_id):
    print(request.form)

    if "user_id" not in session:
        flash("You must be logged in to react.", "error")
        return redirect(url_for("view_doodle", doodle_id=doodle_id))

    emoji = request.form["emoji"]
    encoded_emoji = hex(ord(emoji))[2:]

    db = get_db()
    existing = db.execute(
        "SELECT * FROM reactions WHERE doodle_id = ? AND user_id = ? AND emoji = ?",
        (doodle_id, session["user_id"], encoded_emoji),
    ).fetchone()

    if existing:
        db.execute("DELETE FROM reactions WHERE doodle_id = ? AND user_id = ? AND emoji = ?",
                   (doodle_id, session["user_id"], encoded_emoji))
    else:
        db.execute("INSERT INTO reactions (doodle_id, user_id, emoji, created_at) VALUES (?, ?, ?, ?)",
                   (doodle_id, session["user_id"], encoded_emoji, datetime.utcnow().isoformat()))

    db.commit()
    return redirect(url_for("view_doodle", doodle_id=doodle_id))


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

    return redirect(url_for("view_profile"))


@app.route("/doodle/<int:doodle_id>/comment", methods=["POST"])
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


@app.route("/doodle/<int:doodle_id>/comment/<int:comment_id>/delete", methods=["POST"])
def delete_comment(doodle_id, comment_id):
    if "user_id" not in session:
        return {"error": "Unauthorized"}, 401

    user_id = session["user_id"]
    db = get_db()
    comment = db.execute("SELECT * FROM comments WHERE id = ?", (comment_id,)).fetchone()

    if not comment or comment["user_id"] != user_id:
        return {"error": "Forbidden"}, 403

    db.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
    db.commit()

    return {"success": True}, 200


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
