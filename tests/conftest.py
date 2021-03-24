import pytest

from app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "secret_key"
    app.config["WTF_CSRF_ENABLED"] = False

    with app.test_client() as client:
        yield client
