from flask import session, redirect, url_for
from functools import wraps

from app.models import User


def does_user_have_session() -> bool:
    return 'logged_in' in session and bool(User.get_by_user_id(session.get('logged_in').get('user_id')))


def get_url_for_profile() -> str:
    return url_for('user_routes.get_user', username=session.get('logged_in').get('username'))


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if does_user_have_session():
            return f(session.get('logged_in').get('user_id'), *args, **kwargs)

        return redirect(url_for("auth_routes.sign_in"))

    return decorated


def not_logged_in_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if does_user_have_session():
            return redirect(get_url_for_profile())

        return f(*args, **kwargs)

    return decorated
