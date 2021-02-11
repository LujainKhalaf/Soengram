from typing import Any
import uuid
from app.models import Post
from app.utils.file import get_upload_post_images_dir
from datetime import datetime
from app.utils.file import get_file_extension, get_image_url


def create_post(request: Any, user_id: int) -> None:
    file = request.files['post_image']
    post = post_builder(request.form, file, user_id)

    Post.insert(post)

    upload_post_image(file, post.image_url)


def post_builder(form: Any, file: Any, user_id: int) -> Post:
    description = form.get('description')

    filename = f'{uuid.uuid1().hex}.{get_file_extension(file.filename)}'
    image_url = get_image_url(filename)

    return Post(
        user_id=user_id,
        image_url=image_url,
        description=description,
        created_at=datetime.now()
    )


def upload_post_image(file, image_url) -> None:
    file.save(get_upload_post_images_dir(image_url))

