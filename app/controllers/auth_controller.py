from typing import Any

from flask import request, Blueprint, render_template, redirect, url_for

from app.forms.signup_form import SignupForm
from app.forms.signin_form import SigninForm
from app.services import auth_service
from app.utils.session_decorators import login_required, not_logged_in_required, get_url_for_profile

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/signup', methods=['POST', 'GET'])
@not_logged_in_required
def sign_up() -> Any:
    form = SignupForm()

    if form.validate_on_submit():
        auth_service.sign_up(form)
        auth_service.sign_in(form)

        return redirect(get_url_for_profile())

    return render_template('account/signup.html', form=form)


@auth_routes.route('/signin', methods=['POST', 'GET'])
@not_logged_in_required
def sign_in() -> Any:
    form = SigninForm()

    if form.validate_on_submit():
        auth_service.sign_in(form)

        return redirect(get_url_for_profile())

    return render_template('account/signin.html', form=form)


@auth_routes.route('/signout', methods=['POST'])
@login_required
def sign_out(_) -> Any:
    if request.method == 'POST':
        auth_service.sign_out()
        return redirect(url_for(".sign_in"))
