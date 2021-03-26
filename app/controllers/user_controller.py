from typing import Any
from flask import Blueprint, render_template, jsonify, request
from app.models import User
from app.utils.session import login_required, set_user_feed_offset
from app.services import user_service
from app.models import Post

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/", methods=["GET"])
@login_required
def get_feed(user_id: int) -> Any:
    set_user_feed_offset(Post.BASE_FEED_OFFSET)
    feed = user_service.get_feed(user_id)
    user = User.get_by_user_id(user_id)

    return render_template("feed/base.html", feed=feed, user=user)


@user_routes.route("/next-feed", methods=["GET"])
@login_required
def get_next_feed(user_id: int) -> Any:
    return user_service.get_feed_with_offset(user_id)


@user_routes.route("/<username>", methods=["GET"])
@login_required
def get_user(user_id: int, username: str) -> Any:
    user = User.get_by_username(username)

    if not user:
        return "No user found", 404

    is_me = user.user_id == user_id
    return render_template(
        "account/profile/base.html", user=user, is_me=is_me, my_user_id=user_id
    )


@user_routes.route("/<username>/followers", methods=["GET"])
@login_required
def get_followers(_, username: str) -> Any:
    return user_service.get_followers(username)


@user_routes.route("/<username>/following", methods=["GET"])
@login_required
def get_following(_, username: str) -> Any:
    return user_service.get_following(username)


@user_routes.route("/follow", methods=["POST"])
@login_required
def follow_user(user_id: int) -> Any:
    user_id_to_follow = request.form.get("user_id", type=int) or -1
    return user_service.follow_user(user_id, user_id_to_follow)


@user_routes.route("/unfollow", methods=["POST"])
@login_required
def unfollow_user(user_id: int) -> Any:
    user_id_to_remove = request.form.get("user_id", type=int) or -1
    return user_service.unfollow_user(user_id, user_id_to_remove)
