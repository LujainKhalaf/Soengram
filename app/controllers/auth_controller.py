from typing import Any

from flask import request, Blueprint, render_template, redirect, url_for

from app.forms.signup_form import SignupForm
from app.services import auth_service
from app.utils.session_decorators import login_required, not_logged_in_required
from app.utils.validation import is_email_valid

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/signup', methods=['POST', 'GET'])
@not_logged_in_required
def sign_up() -> Any:
    form = SignupForm()

    if form.validate_on_submit():
        auth_service.sign_up(form)
        return auth_service.sign_in(form.email.data, form.password.data)

    return render_template('account/signup.html', form=form)


@auth_routes.route('/signin', methods=['POST', 'GET'])
@not_logged_in_required
def sign_in() -> Any:
    if request.method == 'GET':
        return render_template('account/signin.html')

    # TODO: Refactor to follow the same structure as def sign_up()
    if request.method == 'POST':
        email, password = request.form.values()

        # TODO: No longer needed with Flask-WTF library handling such validation.
        if not is_email_valid(email):
            return redirect(url_for(".sign_in"))

        return auth_service.sign_in(email, password)


@auth_routes.route('/signout', methods=['POST'])
@login_required
def sign_out(_) -> Any:
    if request.method == 'POST':
        auth_service.sign_out()
        return redirect(url_for(".sign_in"))
