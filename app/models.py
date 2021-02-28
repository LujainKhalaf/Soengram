from __future__ import annotations
from typing import List

from werkzeug.security import check_password_hash

from app.extensions import db
from app.utils.entities import SerializedUser


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='select',
        order_by='desc(Post.created_at)'
    )
    following = db.relationship(
        'User',
        secondary=lambda: followers,
        primaryjoin=lambda: (followers.c.user_id == User.user_id),
        secondaryjoin=lambda: (followers.c.following_id == User.user_id),
        backref='followers'
    )

    def __repr__(self):
        return f'<User username={self.username}>'

    def serialize(self) -> SerializedUser:
        return SerializedUser(
            user_id=self.user_id,
            username=self.username,
            email=self.email,
            full_name=self.full_name,
            created_at=self.created_at
        )

    def get_following(self) -> List[SerializedUser]:
        return [follower.serialize() for follower in self.following]

    def get_followers(self) -> List[SerializedUser]:
        return [follower.serialize() for follower in self.followers]

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

    @staticmethod
    def get_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def add_to_following(user_id: int, user_id_to_follow: int) -> None:
        user = User.get_by_user_id(user_id)
        user_to_follow = User.get_by_user_id(user_id_to_follow)
        user.following.append(user_to_follow)

        db.session.commit()

    @staticmethod
    def remove_from_following(user_id: int, user_id_to_remove: int) -> None:
        user = User.get_by_user_id(user_id)
        user_to_remove = User.get_by_user_id(user_id_to_remove)
        user.following.remove(user_to_remove)

        db.session.commit()

    @staticmethod
    def is_authenticated(user_by_email: User, password: User) -> bool:
        if not user_by_email:
            return False

        return check_password_hash(user_by_email.password, password)

    @staticmethod
    def get_feed_by_user_id(user_id: int) -> List[Post]:
        query = f'''
            SELECT
                post_id,
                post.user_id,
                image_url,
                description,
                created_at
            FROM post
            JOIN followers f ON post.user_id = f.following_id
            WHERE {user_id} = f.user_id
            ORDER BY post.created_at DESC
            LIMIT 50
        '''

        raw_feed = db.session.execute(query)

        return [Post(**dict(post.items())) for post in raw_feed]


class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Post post_id={self.post_id}>'

    @staticmethod
    def insert(post: Post) -> None:
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def get_by_post_id(post_id: int) -> Post:
        return Post.query.get(post_id)

    @staticmethod
    def delete(post: Post) -> None:
        db.session.delete(post)
        db.session.commit()

    @staticmethod
    def is_post_owned_by_user(post: Post, user_id: int) -> bool:
        return post and post.user_id == user_id


followers = db.Table(
    'followers',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('following_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
)
