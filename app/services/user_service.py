from typing import List

from flask import jsonify

from app.models import User, Post
from app.utils.entities import JSONResponse


def get_feed(user_id: int) -> List[Post]:
    return User.get_feed_by_user_id(user_id)


def get_followers(username: str) -> JSONResponse:
    user = User.get_by_username(username)

    if not user:
        return jsonify('User not found'), 404

    return jsonify(followers=user.get_followers()), 200


def get_following(username: str) -> JSONResponse:
    user = User.get_by_username(username)

    if not user:
        return jsonify('User not found'), 404

    return jsonify(following=user.get_following()), 200


def follow_user(user_id: int, user_id_to_follow: int) -> JSONResponse:
    if user_id_to_follow == user_id:
        return jsonify('Invalid parameters'), 400

    User.add_to_following(user_id, user_id_to_follow)
    return jsonify(''), 204


def unfollow_user(user_id: int, user_id_to_remove: int) -> JSONResponse:
    if user_id_to_remove == user_id:
        return jsonify('Invalid parameters'), 400

    User.remove_from_following(user_id, user_id_to_remove)
    return jsonify(''), 204
