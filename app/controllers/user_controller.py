from typing import Any
from flask import Blueprint, render_template, jsonify, request
from app.models import User
from app.utils.session_decorators import login_required
from app.services import user_service

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/<username>', methods=['GET'])
@login_required
def get_user(user_id: int, username: str) -> Any:
    user = User.get_by_username(username)

    if not user:
        return 'No user found', 404

    is_me = user.user_id == user_id
    return render_template('account/profile/base.html', user=user, is_me=is_me)


@user_routes.route('/<username>/followers', methods=['GET'])
@login_required
def get_followers(_, username: str) -> Any:
    return user_service.get_followers(username)


@user_routes.route('/<username>/following', methods=['GET'])
@login_required
def get_following(_, username: str) -> Any:
    return user_service.get_following(username)


@user_routes.route('/follow', methods=['POST'])
@login_required
def follow_user(user_id: int) -> Any:
    try:
        user_id_to_follow = request.form.get('user_id_to_follow')
        return user_service.follow_user(user_id, user_id_to_follow)
    except Exception:
        return jsonify('User not found'), 404


@user_routes.route('/unfollow', methods=['POST'])
@login_required
def unfollow_user(user_id: int) -> Any:
    try:
        user_id_to_remove = request.form.get('user_id_to_remove')
        return user_service.unfollow_user(user_id, user_id_to_remove)
    except Exception:
        return jsonify('User not found'), 404
