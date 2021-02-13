from typing import Any
from flask import Blueprint, render_template, session
from app.models import User
from app.utils.session_decorators import session_required


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/<username>', methods=['GET'])
@session_required
def get_user(username) -> Any:
    user = User.get_by_username(username)
    if user:
        is_me = user.user_id == session['token']
        return render_template('profile.html', user=user, is_me=is_me), 200
    else:
        return '', 404
    
