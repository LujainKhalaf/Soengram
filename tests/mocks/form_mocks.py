from collections import namedtuple
from dataclasses import dataclass


@dataclass
class SignupFormMock:
    Field = namedtuple("Field", ["data"])

    username = Field("username1")
    email = Field("test@email.com")
    full_name = Field("first last")
    password = Field("password")
