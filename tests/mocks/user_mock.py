from werkzeug.security import generate_password_hash

from app.models import User
from app.utils.entities import SerializedUser


def create_mock_user() -> User:
    return User(
        user_id=1,
        username='username1',
        full_name='first last',
        email='test@email.com',
        password=generate_password_hash('password')
    )


def create_mock_serialized_user() -> SerializedUser:
    return create_mock_user().serialize()
