from flask import request, session, abort


def check_csrf():
    form_csrf_token = request.form.get("csrf_token")
    if not form_csrf_token:
        abort(403)

    session_csrf_token = session.get("csrf_token")
    if not session_csrf_token:
        abort(403)

    if form_csrf_token != session_csrf_token:
        abort(403)
