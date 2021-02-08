import re


def is_email_valid(email: str) -> bool:
    regex = r'^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'

    return bool(re.match(regex, email))
