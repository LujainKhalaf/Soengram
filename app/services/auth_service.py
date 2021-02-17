from datetime import datetime
from typing import Any

from flask import session, redirect, url_for
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User
from app.utils.session_decorators import get_url_for_profile


def sign_up(form: FlaskForm) -> None:
    user = User(username=form.username.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data),
                full_name=form.full_name.data,
                created_at=datetime.now())

    User.insert(user)


def sign_in(email: str, password: str) -> Any:
    user = User.get_by_email(email)

    if user:
        is_authenticated = check_password_hash(user.password, password)
        if is_authenticated:
            session['logged_in'] = dict(user_id=user.user_id, username=user.username)
            return redirect(get_url_for_profile())
    raise Exception('Incorrect username and/or password.')
    return redirect(url_for("auth_routes.sign_in"))


def sign_out() -> None:
    session.pop('logged_in', None)
