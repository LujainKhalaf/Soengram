from os.path import join, dirname, realpath
from config import Config


def get_file_extension(filename) -> str:
    return filename.rsplit('.', 1)[1].lower()


def get_app_root_dir() -> str:
    return join(dirname(realpath('app.py')), 'app/')


def get_post_images_dir() -> str:
    return join(get_app_root_dir(), Config.POST_UPLOAD_FOLDER)
