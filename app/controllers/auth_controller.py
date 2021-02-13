from typing import Tuple

from flask import request, Blueprint, render_template, redirect

from app.services import auth_service
from app.utils.session_decorators import session_required
from app.utils.validation import is_email_valid

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/signup', methods=['POST', 'GET'])
def sign_up() -> Tuple[str, int]:
    form = SignupForm();

    if form.validate_on_submit():
        auth_service.sign_up(form)
        auth_service.sign_in(form.username.data, form.password.data)

        return redirect("/")

    return render_template('/account/signup.html', form=form)


@auth_routes.route('/signin', methods=['POST'])
def sign_in() -> Tuple[str, int]:
    # TODO: Refactor to follow the same structure as def sign_up()
    if request.method == 'POST':
        email, password = request.form.values()

        # TODO: No longer needed with Flask-WTF library handling such validation.
        if not is_email_valid(email):
            return '', 400

        return auth_service.sign_in(email, password)


@auth_routes.route('/signout', methods=['POST'])
@session_required
def sign_out(user_id) -> Tuple[str, int]:
    if request.method == 'POST':
        auth_service.sign_out()

        return '', 204
