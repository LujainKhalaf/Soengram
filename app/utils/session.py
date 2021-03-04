from flask import session, redirect, url_for
from functools import wraps

from app.models import User, Post
from app.utils.entities import UserSession


SESSION_KEY = 'logged_in'
FEED_OFFSET_KEY = 'feed_offset'


def get_user_session() -> UserSession:
    session_dict = session.get(SESSION_KEY)

    return UserSession(
        user_id=session_dict.get('user_id'),
        username=session_dict.get('username')
    )


def get_feed_offset() -> int:
    return session.get(FEED_OFFSET_KEY, 0)


def increment_user_feed_offset() -> None:
    set_user_feed_offset(get_feed_offset() + Post.FEED_OFFSET_INCREMENT)


def set_user_feed_offset(offset: int) -> None:
    session[FEED_OFFSET_KEY] = offset


def does_user_have_session() -> bool:
    return SESSION_KEY in session and bool(User.get_by_user_id(get_user_session().user_id))


def get_url_for_profile() -> str:
    return url_for('user_routes.get_user', username=get_user_session().username)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if does_user_have_session():
            return f(get_user_session().user_id, *args, **kwargs)

        return redirect(url_for("auth_routes.sign_in"))

    return decorated


def not_logged_in_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if does_user_have_session():
            return redirect(get_url_for_profile())

        return f(*args, **kwargs)

    return decorated
