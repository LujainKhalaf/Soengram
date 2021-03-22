from typing import List

from app.models import Post


def create_mock_post(post_id: int = 1) -> Post:
    return Post(
        post_id=post_id,
        user_id=1,
        image_url='url',
        description='description'
    )


def mock_user_service_get_feed(_) -> List[Post]:
    return [create_mock_post(i) for i in range(10)]
