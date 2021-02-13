from typing import Any
from flask import request, Blueprint, render_template, redirect, url_for, flash
from app.services import post_service
from app.utils.file import FORM_POST_IMAGE
from app.utils.session_decorators import session_required
from app.utils.validation import is_post_image_valid

post_routes = Blueprint('post_routes', __name__)


@post_routes.route('/post', methods=['GET', 'POST'])
@session_required
def create_post(user_id: int) -> Any:
    if request.method == 'GET':
        return render_template('create_post.html', message='Hello World!')

    if request.method == 'POST':

        if not is_post_image_valid(request.files):
            flash('A valid image is required to make a post')
            return redirect(request.url)

        file = request.files[FORM_POST_IMAGE]

        post = post_service.post_builder(request, user_id)
        post_service.create_post(post, file)

        return redirect(url_for("index_routes.index"))
