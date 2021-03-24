import os


class Config(object):
    # General
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    POST_UPLOAD_FOLDER = os.environ.get("POST_UPLOAD_FOLDER")

    # Database
    SQLALCHEMY_DATABASE_URI = (
        "{type}://{username}:{password}@{host}:{port}/{db}".format(
            type=os.environ.get("DB_TYPE"),
            username=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            db=os.environ.get("DB_DATABASE"),
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
