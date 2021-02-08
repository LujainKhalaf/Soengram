from typing import Tuple
from flask import request, Blueprint
from app.models.user import User
from app.services import auth_service
from app.utils.validation import is_email_valid
from app.utils.session_decorators import session_required

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/signup', methods=['POST'])
def sign_up() -> Tuple[str, int]:
    if request.method == 'POST':
        full_name, username, email, password = request.form.values()

        if not is_email_valid(email):
            return '', 400

        user = User(full_name=full_name, username=username, email=email)
        auth_service.sign_up(user, password)

        return '', 201


@auth_routes.route('/signin', methods=['POST'])
def sign_in() -> Tuple[str, int]:
    if request.method == 'POST':
        email, password = request.form.values()

        if not is_email_valid(email):
            return '', 400

        return auth_service.sign_in(email, password)


@auth_routes.route('/signout', methods=['POST'])
@session_required
def sign_out(user_id) -> Tuple[str, int]:
    if request.method == 'POST':
        auth_service.sign_out()

        return '', 204
