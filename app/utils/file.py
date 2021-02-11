from os.path import join, dirname, realpath
from config import Config


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
FORM_POST_IMAGE = 'post_image'


def get_file_extension(filename) -> str:
    return filename.rsplit('.', 1)[1].lower()


def get_app_root_dir() -> str:
    return join(dirname(realpath('app.py')), 'app/')


def get_image_url_dir(image_url) -> str:
    return join(get_app_root_dir(), image_url)


def get_image_url(filename) -> str:
    return join(Config.POST_UPLOAD_FOLDER, filename)
