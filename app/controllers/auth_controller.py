from typing import Tuple
from flask import request, Blueprint, render_template
from app.services import auth_service
from app.utils.validation import is_email_valid
from app.utils.session_decorators import session_required

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/signup', methods=['POST', 'GET'])
def sign_up() -> Tuple[str, int]:
    if request.method == 'POST':
        full_name, username, email, password = request.form.values()

        if not is_email_valid(email):
            return render_template('signup.html', error='Invalid email address')

        auth_service.sign_up(full_name, username, email, password)

        return render_template('index.html', message='Hello World!')

    if request.method == 'GET':
        return render_template('signup.html')


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
