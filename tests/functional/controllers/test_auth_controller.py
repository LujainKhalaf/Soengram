import flask

from app.utils.session import SESSION_KEY
from tests.mocks.user_mock import mock_user_get_by_user_id


def test_signin_page(client):
    rv = client.get('/account/signin')
    assert b'Sign In - Soengram' in rv.data


def test_signup_page(client):
    rv = client.get('/account/signup')
    assert b'Sign Up - Soengram' in rv.data


def test_signout(mocker, client):
    with client.session_transaction() as sess:
        sess[SESSION_KEY] = {
            'user_id': 1,
            'username': 'username1'
        }

    mocker.patch(
        'app.models.User.get_by_user_id',
        mock_user_get_by_user_id
    )

    rv = client.post('/account/signout', follow_redirects=True)
    assert b'Sign In - Soengram' in rv.data
    assert SESSION_KEY not in flask.session
