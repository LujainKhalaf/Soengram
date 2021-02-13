from typing import Tuple
from flask import Blueprint
from app.models import User
from app.utils.session_decorators import session_required


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/<username>')
@session_required
def get_user(username) -> Tuple[str, int]:
    user = User.get_by_username(username)
    if user:
        return '', 200
    else:
        return '', 204

