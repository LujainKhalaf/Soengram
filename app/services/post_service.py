from typing import Any, Tuple
import uuid

from flask import jsonify

from app.forms.post_form import CreatePostForm
from app.models import Post
from app.utils.file import get_image_url_dir
from datetime import datetime
from app.utils.file import get_file_extension, get_image_url


def create_post(user_id: int, form: CreatePostForm) -> None:
    post = post_builder(user_id, form)

    Post.insert(post)
    upload_post_image(form.post_image.data, post.image_url)


def delete_post(user_id: int, post_id: int) -> Tuple[str, int]:
    post = Post.get_by_post_id(post_id)

    if not Post.is_post_owned_by_user(post, user_id):
        return jsonify('Post not found'), 404

    Post.delete(post)

    return jsonify('Post deleted'), 204


def upload_post_image(file: Any, image_url: str) -> None:
    file.save(get_image_url_dir(image_url))


def post_builder(user_id: int, form: CreatePostForm) -> Post:
    file = form.post_image.data
    filename = f'{uuid.uuid1().hex}.{get_file_extension(file.filename)}'

    return Post(
        user_id=user_id,
        image_url=get_image_url(filename),
        description=form.description.data,
        created_at=datetime.now()
    )
