from flask import (
    Flask,
    g,
    send_file,
    redirect,
    url_for,
    session,
)

import config
from config import USER_IMAGE_UPLOADS_PATH, DATABASE_PATH
from database import get_db
from routes.doodle.doodle_route import doodle_blueprint
from routes.home_route import home_blueprint
from routes.login.login_route import login_blueprint
from routes.profile.profile_route import profile_blueprint
from routes.register.register_route import register_blueprint
from routes.search.search_route import search_blueprint
from routes.submit.submit_route import submit_blueprint

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

app.register_blueprint(home_blueprint)
app.register_blueprint(doodle_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(submit_blueprint)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.page"))


@app.route("/image/<filename>")
def serve_image(filename):
    if (safe_path := USER_IMAGE_UPLOADS_PATH / filename).exists():
        return send_file(safe_path)
    else:
        return "File not found", 404


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def init_db():
    print("Initializing database")
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()
        print("Database created")


if __name__ == "__main__":
    if not DATABASE_PATH.exists():
        init_db()
    app.run()
