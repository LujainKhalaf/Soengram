from typing import Any
from flask import Blueprint, render_template, jsonify
from app.models import User
from app.utils.session_decorators import login_required

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/<username>', methods=['GET'])
@login_required
def get_user(user_id: int, username: str) -> Any:
    user = User.get_by_username(username)
    if user:
        is_me = user.user_id == user_id
        return render_template('account/profile.html', user=user, is_me=is_me)
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
