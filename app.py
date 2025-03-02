from flask import (
    Flask,
    g,
    send_file,
    redirect,
    url_for,
    session,
    render_template,
)
import markupsafe
import config
from config import USER_IMAGE_UPLOADS_PATH, DATABASE_PATH
from routes.doodle.doodle_route import doodle_blueprint
from routes.home_route import home_blueprint
from routes.login.login_route import login_blueprint
from routes.profile.profile_route import profile_blueprint
from routes.register.register_route import register_blueprint
from routes.search.search_route import search_blueprint
from routes.submit.submit_route import submit_blueprint

if not DATABASE_PATH.exists():
    print(
        f"Database file not found: {DATABASE_PATH}. Initialize the database by running `python database.py`"
    )
    exit(1)

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

app.register_blueprint(home_blueprint)
app.register_blueprint(doodle_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(profile_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(submit_blueprint)


@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.page"))


@app.errorhandler(404)
def not_found(e):
    """General 404 error handler."""
    return render_template("not-found.html"), 404


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


if __name__ == "__main__":
    app.run()
