from app.models import Post


def create_mock_post() -> Post:
    return Post(
        post_id=1,
        user_id=1,
        image_url='url',
        description='description'
    )
