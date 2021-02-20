from typing import Any
from flask import request, Blueprint, render_template, redirect
from app.services import post_service
from app.utils.session_decorators import login_required, get_url_for_profile
from app.models import Post
from app.forms.post_form import PostForm

post_routes = Blueprint('post_routes', __name__)


@post_routes.route('/post', methods=['GET', 'POST'])
@login_required
def create_post(user_id: int) -> Any:
    form = PostForm()

    if form.validate_on_submit():
        post_service.create_post(user_id, form)

        return redirect(get_url_for_profile())

    return render_template('post/create_post.html', form=form)


@post_routes.route('/delete', methods=['POST'])
@login_required
def delete_post(user_id: int) -> Any:
    post_id = request.form.values()
    post = Post.get_by_post_id(post_id)
    if post:
        if post.user_id == user_id:
            Post.delete(post)
            return redirect(get_url_for_profile())
    return '', 404

