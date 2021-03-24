from __future__ import annotations
from typing import List

from sqlalchemy.orm import synonym
from werkzeug.security import check_password_hash

from app.extensions import db
from app.utils.entities import SerializedUser


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    posts: List[Post] = db.relationship(
        "Post", back_populates="user", lazy="select", order_by="desc(Post.created_at)"
    )
    following = db.relationship(
        "User",
        secondary=lambda: followers,
        primaryjoin=lambda: (followers.c.user_id == User.user_id),
        secondaryjoin=lambda: (followers.c.following_id == User.user_id),
        backref="followers",
    )

    def __repr__(self):
        return f"<User username={self.username}>"

    def serialize(self) -> SerializedUser:
        return SerializedUser(
            user_id=self.user_id,
            username=self.username,
            email=self.email,
            full_name=self.full_name,
            created_at=self.created_at,
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
    def is_authenticated(user_by_email: User, password: str) -> bool:
        if not user_by_email:
            return False

        return check_password_hash(user_by_email.password, password)

    @staticmethod
    def get_feed_by_user_id(user_id: int, offset: int) -> List[Post]:
        query = f"""
            SELECT post_id
            FROM post
            JOIN followers f ON post.user_id = f.following_id
            WHERE {user_id} = f.user_id
            ORDER BY post.created_at DESC
            OFFSET {offset} LIMIT {Post.FEED_OFFSET_INCREMENT}
        """

        # will be an iterable of rows with 1 element being the post_id
        rows = db.session.execute(query)

        return [Post.get_by_post_id(row[0]) for row in rows]


class Post(db.Model):
    __tablename__ = "post"

    BASE_FEED_OFFSET = 0
    FEED_OFFSET_INCREMENT = 10

    post_id = db.Column(db.Integer, primary_key=True)
    id = synonym("post_id")
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2200), nullable=False)
    text = synonym("description")
    created_at = db.Column(db.DateTime, nullable=False)
    user = db.relationship("User", back_populates="posts", lazy="select")
    comments: List[Comment] = db.relationship(
        "Comment", backref="post", lazy="select", order_by="desc(Comment.created_at)"
    )

    def __repr__(self):
        return f"<Post post_id={self.post_id}>"

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


class Comment(db.Model):
    __tablename__ = "comment"

    comment_id = db.Column(db.Integer, primary_key=True)
    id = synonym("comment_id")
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.post_id"), nullable=False)
    comment_text = db.Column(db.String(2200), nullable=False)
    text = synonym("comment_text")
    created_at = db.Column(db.DateTime, nullable=False)
    user = db.relationship("User", backref="comments", lazy="select")

    def __repr__(self):
        return f"<Comment comment_id={self.comment_id}>"

    @staticmethod
    def insert(comment: Comment) -> None:
        db.session.add(comment)
        db.session.commit()

    @staticmethod
    def get_by_comment_id(comment_id: int) -> Post:
        return Comment.query.get(comment_id)

    @staticmethod
    def delete(comment: Comment) -> None:
        db.session.delete(comment)
        db.session.commit()

    @staticmethod
    def is_comment_owned_by_user(comment: Comment, user_id: int) -> bool:
        return comment and comment.user_id == user_id


followers: db.Table = db.Table(
    "followers",
    db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
    db.Column(
        "following_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True
    ),
)
