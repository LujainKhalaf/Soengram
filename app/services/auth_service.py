from datetime import datetime

from flask import session
from werkzeug.security import generate_password_hash

from app.forms.signin_form import SigninForm
from app.forms.signup_form import SignupForm
from app.models import User
from app.utils.entities import UserSession
from app.utils.session import SESSION_KEY


def sign_up(form: SignupForm) -> None:
    user = user_builder(form)

    User.insert(user)


def sign_in(form: SigninForm) -> None:
    user = User.get_by_email(form.email.data)

    session[SESSION_KEY] = user_session_builder(user)


def sign_out() -> None:
    session.pop(SESSION_KEY, None)


def user_builder(form: SignupForm) -> User:
    return User(
        username=form.username.data,
        email=form.email.data,
        password=generate_password_hash(form.password.data),
        full_name=form.full_name.data,
        created_at=datetime.now()
    )


def user_session_builder(user: User) -> UserSession:
    return UserSession(
        user_id=user.user_id,
        username=user.username
    )
