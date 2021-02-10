from flask import session
from functools import wraps
from app.models import User


def session_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'token' in session:
            does_user_session_exist = bool(User.get_by_user_id(session.get('token')))
            if does_user_session_exist:
                return f(session.get('token'), *args, **kwargs)

        return '', 404

    return decorated
