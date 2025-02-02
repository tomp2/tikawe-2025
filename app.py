import sqlite3
from pathlib import Path

from flask import Flask, g, send_file, render_template, request, redirect, url_for, session
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
    query = "SELECT * FROM doodles ORDER BY views DESC LIMIT 10"
    doodles = db.execute(query).fetchall()
    return render_template("home.html", doodles=doodles)


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
