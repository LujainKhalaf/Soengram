from werkzeug.security import generate_password_hash
from datetime import datetime
from app.models.user import User
from app.extensions import db


def sign_up(user: User, password: str) -> None:
    hashed_password = generate_password_hash(password)
    user.password = hashed_password

    user.created_at = datetime.now()

    db.session.add(user)
    db.session.commit()
