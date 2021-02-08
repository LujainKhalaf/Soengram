from flask import Flask
from app.app import create_app


def test_should_return_flask_app() -> None:
    app = create_app()
    assert type(app) is Flask
