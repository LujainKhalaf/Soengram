from app.models import User, Post, Comment
from app.utils.entities import SerializedUser
from tests.mocks.comment_mock import create_mock_comment
from tests.mocks.post_mock import create_mock_post
from tests.mocks.user_mock import create_mock_user, create_mock_serialized_user


def test_user_constructor():
    user = create_mock_user()

    assert type(user) is User
    assert user.user_id == 1
    assert user.username == "username1"


def test_user_serialize():
    serialized_user = create_mock_serialized_user()

    assert type(serialized_user) is SerializedUser
    assert serialized_user.user_id == 1
    assert not hasattr(serialized_user, "password")


def test_is_authenticated():
    user = create_mock_user()

    assert User.is_authenticated(user, "password")


def test_post_constructor():
    post = create_mock_post()

    assert type(post) is Post
    assert post.post_id == 1
    assert post.user_id == 1
    assert post.description == "description"


def test_is_post_owned_by_user():
    post = create_mock_post()

    assert Post.is_post_owned_by_user(post, 1)


def test_comment_constructor():
    comment = create_mock_comment()

    assert type(comment) is Comment
    assert comment.comment_id == 1
    assert comment.post_id == 1
    assert comment.user_id == 1
    assert comment.comment_text == "comment text"


def test_is_comment_owned_by_user():
    comment = create_mock_comment()

    assert Comment.is_comment_owned_by_user(comment, 1)
