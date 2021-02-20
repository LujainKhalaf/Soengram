from typing import Any
from flask import Blueprint, render_template, jsonify, request
from app.models import User
from app.utils.session_decorators import login_required

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/<username>', methods=['GET'])
@login_required
def get_user(user_id: int, username: str) -> Any:
    user = User.get_by_username(username)
    if user:
        is_me = user.user_id == user_id
        return render_template('account/profile/base.html', user=user, is_me=is_me, followers=get_followers(username))
    else:
        return '', 404


@user_routes.route('/<username>/followers', methods=['GET'])
@login_required
def get_followers(_, username: str) -> Any:
    user = User.get_by_username(username)

    if not user:
        return '', 404

    followers = [follower.serialize_as_follower() for follower in user.get_followers()]
    return jsonify(followers=followers)


@user_routes.route('/<username>/following', methods=['GET'])
@login_required
def get_following(_, username: str) -> Any:
    user = User.get_by_username(username)

    if not user:
        return '', 404

    following = [following.serialize_as_follower() for following in user.get_following()]
    return jsonify(following=following)


@user_routes.route('/follow', methods=['POST'])
@login_required
def follow_user(user_id: int) -> Any:
    user_id_to_follow: int = request.form.values()
    if user_id_to_follow == user_id:
        return '', 400
    try:
        User.add_to_following(user_id, user_id_to_follow)
        return '', 204
    except Exception:
        return '', 404


@user_routes.route('/unfollow', methods=['POST'])
@login_required
def unfollow_user(user_id: int) -> Any:
    user_id_to_remove: int = request.form.values()
    if user_id_to_remove == user_id:
        return '', 400
    try:
        User.remove_from_following(user_id, user_id_to_remove)
        return '', 204
    except Exception:
        return '', 404

