from flask import Blueprint
from datetime import datetime

jinga = Blueprint("jinga", __name__)


@jinga.app_template_filter("postdateformat")
def post_date_format(value):
    if value is None:
        return ""

    if datetime.today().year == int(value.strftime("%Y")):
        return value.strftime("%B %d").lstrip("0").replace(" 0", " ")

    return value.strftime("%B %d, %Y").lstrip("0").replace(" 0", " ")


@jinga.app_template_filter("uppercase")
def uppercase(value):
    return value.upper()
