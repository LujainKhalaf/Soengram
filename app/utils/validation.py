import re
from app.utils.file import get_file_extension, FORM_POST_IMAGE, ALLOWED_EXTENSIONS


def is_email_valid(email: str) -> bool:
    regex = r'^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'

    return bool(re.match(regex, email))


def is_file_allowed(filename) -> bool:
    return '.' in filename and get_file_extension(filename) in ALLOWED_EXTENSIONS

