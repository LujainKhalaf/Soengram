from flask import Flask
from app import index
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(index.index_controller.bp)
    return None