from datetime import datetime
from typing import Tuple

from flask import session
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User


class LoggedInUser:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


def sign_up(form: FlaskForm) -> None:
    user = User(username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data),
                full_name=form.full_name.data,
                created_at=datetime.now())

    User.insert(user)


def sign_in(email: str, password: str) -> Tuple[str, int]:
    user = User.get_by_email(email)

    if user:
        is_authenticated = check_password_hash(user.password, password)

        if is_authenticated:
            logged_in_user = LoggedInUser(user.user_id, user.username)
            session['logged_in'] = logged_in_user.__dict__
            return '', 204

    return '', 404


def sign_out() -> None:
    session.pop('logged_in', None)
