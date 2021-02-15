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
        return render_template('account/profile/base.html', user=user, is_me=is_me)
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


@user_routes.route('/follow', methods=['GET', 'POST'])
@login_required
def follow_user_api(user_id: int) -> Any:
    try:
        user_id_to_follow = int(request.args.get('id'))
    except ValueError:
        return '', 404
    user = User.get_by_user_id(user_id)
    user_to_follow = User.get_by_user_id(user_id_to_follow)
    if user and user_to_follow and user_id != user_id_to_follow:
        User.add_to_following(user_id, user_id_to_follow)
        return jsonify(user_id=user_id, user_id_to_follow=user_id_to_follow, following=True)
    return '', 404


@user_routes.route('/unfollow', methods=['GET', 'POST'])
@login_required
def unfollow_user_api(user_id: int) -> Any:
    try:
        user_id_to_remove = int(request.args.get('id'))
    except ValueError:
        return '', 404
    user = User.get_by_user_id(user_id)
    user_to_remove = User.get_by_user_id(user_id_to_remove)
    if user and user_to_remove and user_id != user_id_to_remove:
        User.remove_from_following(user_id, user_id_to_remove)
        return jsonify(user_id=user_id, user_id_to_remove=user_id_to_remove, following=False)
    return '', 404
