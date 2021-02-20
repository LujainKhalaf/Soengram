from typing import Tuple, Any

from flask import jsonify

from app.models import User


def get_followers(username: str) -> Tuple[Any, int]:
    user = User.get_by_username(username)

    if not user:
        return jsonify('User not found'), 404

    return jsonify(followers=user.get_followers()), 200


def get_following(username: str) -> Tuple[Any, int]:
    user = User.get_by_username(username)

    if not user:
        return jsonify('User not found'), 404

    return jsonify(following=user.get_following()), 200


def follow_user(user_id: int, user_id_to_follow: int) -> Tuple[Any, int]:
    if user_id_to_follow == user_id:
        return jsonify('Invalid parameters'), 400

    User.add_to_following(user_id, user_id_to_follow)
    return '', 204


def unfollow_user(user_id: int, user_id_to_remove: int) -> Tuple[Any, int]:
    if user_id_to_remove == user_id:
        return jsonify('Invalid parameters'), 400

    User.remove_from_following(user_id, user_id_to_remove)
    return '', 204
