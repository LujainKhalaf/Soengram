from app.models import Post
from app.utils.file import get_upload_post_images_dir
from datetime import datetime


def upload_post_image(file, image_url) -> None:
    file.save(get_upload_post_images_dir(image_url))


def create_post(user_id: int, image_url: str, description: str) -> None:
    post = Post(
        user_id=user_id,
        image_url=image_url,
        description=description,
        created_at=datetime.now()
    )

    Post.insert(post)
