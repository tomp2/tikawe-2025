import sqlite3
from pathlib import Path

from flask import Flask, g, send_file

import config

app = Flask(__name__)
app.secret_key = config.secret_key
DATABASE = Path("data.db")
USER_IMAGE_UPLOADS = Path("user_image_uploads")

if not USER_IMAGE_UPLOADS.exists():
    USER_IMAGE_UPLOADS.mkdir()


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


@app.route('/image/<filename>')
def serve_image(filename):
    if (safe_path := USER_IMAGE_UPLOADS / filename).exists():
        return send_file(safe_path)
    else:
        return 'File not found', 404


if __name__ == '__main__':
    if not DATABASE.exists():
        init_db()
    app.run()
