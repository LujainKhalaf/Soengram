from flask import session
from functools import wraps
from app.models import User


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'logged_in' in session:
            does_user_session_exist = bool(User.get_by_user_id(session.get('logged_in')['user_id']))
            if does_user_session_exist:
                return f(session.get('logged_in'), *args, **kwargs)

        return '', 404

    return decorated
