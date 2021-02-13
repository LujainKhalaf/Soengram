from __future__ import annotations
from app.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    posts = db.relationship('Post', backref='user', lazy='select')

    def __repr__(self):
        return f'<User username={self.username}>'

    @staticmethod
    def insert(user: User) -> None:
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_user_id(user_id: int) -> User:
        return User.query.get(user_id)


class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Post post_id={self.post_id}>'

    @staticmethod
    def insert(post: Post) -> None:
        db.session.add(post)
        db.session.commit()
