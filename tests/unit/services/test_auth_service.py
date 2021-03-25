from typing import cast

from werkzeug.security import check_password_hash

from app.forms.signup_form import SignupForm
from app.models import User
from app.services.auth_service import user_session_builder, user_builder
from app.utils.entities import UserSession
from tests.mocks.form_mocks import SignupFormMock
from tests.mocks.user_mock import create_mock_user


def test_user_session_builder():
    user = create_mock_user()
    user_session = user_session_builder(user)

    assert type(user_session) is UserSession
    assert user_session.user_id == 1
    assert user_session.username == "username1"


def test_user_builder():
    form = SignupFormMock()
    user = user_builder(cast(SignupForm, form))

    assert type(user) is User
    assert user.username == "username1"
    assert check_password_hash(user.password, "password")
