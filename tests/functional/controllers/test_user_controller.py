from app.utils.session import SESSION_KEY
from tests.mocks.post_mock import mock_user_service_get_feed
from tests.mocks.user_mock import mock_user_get_by_username, mock_user_get_by_user_id


def test_feed(mocker, client):
    with client.session_transaction() as sess:
        sess[SESSION_KEY] = {"user_id": 1, "username": "username1"}

    mocker.patch("app.models.User.get_by_user_id", mock_user_get_by_user_id)

    mocker.patch("app.services.user_service.get_feed", mock_user_service_get_feed)

    rv = client.get("/")
    assert b"data-post-id=2" in rv.data


def test_profile(mocker, client):
    with client.session_transaction() as sess:
        sess[SESSION_KEY] = {"user_id": 1, "username": "username1"}

    mocker.patch("app.models.User.get_by_user_id", mock_user_get_by_user_id)

    mocker.patch("app.models.User.get_by_username", mock_user_get_by_username)

    rv = client.get("/username1")
    assert b'<h2 class="profile-user-name">username1' in rv.data
