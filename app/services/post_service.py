from typing import Any
import uuid

from app.forms.post_form import PostForm
from app.models import Post
from app.utils.file import get_image_url_dir, FORM_POST_IMAGE
from datetime import datetime
from app.utils.file import get_file_extension, get_image_url


def create_post(post: Post, file: Any) -> None:
    Post.insert(post)

    upload_post_image(file, post.image_url)


def upload_post_image(file: Any, image_url: str) -> None:
    file.save(get_image_url_dir(image_url))


def post_builder(form: PostForm, user_id: int) -> Post:
    file = form.post_image.data
    description = form.description.data

    filename = f'{uuid.uuid1().hex}.{get_file_extension(file.filename)}'
    image_url = get_image_url(filename)

    return Post(
        user_id=user_id,
        image_url=image_url,
        description=description,
        created_at=datetime.now()
    )
