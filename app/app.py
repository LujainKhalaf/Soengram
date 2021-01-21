from flask import Flask
from app import index

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(index.index_controller.bp)
    return None
