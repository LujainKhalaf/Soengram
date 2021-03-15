from flask import Flask
from app.controllers import auth_controller, post_controller, user_controller, comment_controller
from app.extensions import db, migrate
from app.utils.ui import template_filters


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    register_extensions(app)
    register_blueprints(app)
    register_template_filters(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(auth_controller.auth_routes, url_prefix='/account')
    app.register_blueprint(post_controller.post_routes)
    app.register_blueprint(comment_controller.comment_routes)
    app.register_blueprint(user_controller.user_routes)


def register_template_filters(app):
    app.register_blueprint(template_filters.jinga)