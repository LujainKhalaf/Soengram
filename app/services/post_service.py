from typing import Any
import uuid

from app.forms.post_form import PostForm
from app.models import Post
from app.utils.file import get_image_url_dir
from datetime import datetime
from app.utils.file import get_file_extension, get_image_url


def create_post(user_id: int, form: PostForm) -> None:
    post = post_builder(user_id, form)

    Post.insert(post)
    upload_post_image(form.post_image.data, post.image_url)


def upload_post_image(file: Any, image_url: str) -> None:
    file.save(get_image_url_dir(image_url))


def post_builder(user_id: int, form: PostForm) -> Post:
    file = form.post_image.data
    filename = f'{uuid.uuid1().hex}.{get_file_extension(file.filename)}'

    return Post(
        user_id=user_id,
        image_url=get_image_url(filename),
        description=form.description.data,
        created_at=datetime.now()
    )
