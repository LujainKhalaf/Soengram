from datetime import datetime
from typing import Tuple

from flask import session
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import User


def sign_up(form: FlaskForm) -> None:
    user = User(username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data),
                full_name=form.full_name.data,
                created_at=datetime.now())

    User.insert(user)


def sign_in(email: str, password: str) -> Tuple[str, int]:
    user_by_email = User.get_by_email(email)

    if user_by_email:
        is_authenticated = check_password_hash(user_by_email.password, password)

        if is_authenticated:
            session['token'] = user_by_email.user_id
            return '', 204

    return '', 404


def sign_out() -> None:
    session.pop('token', None)
