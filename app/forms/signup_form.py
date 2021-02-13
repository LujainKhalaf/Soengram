from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms_validators import AlphaNumeric

from app.models import User


class SignupForm(FlaskForm):
    EMAIL_LENGTH_MAX = 50
    FULL_NAME_LENGTH_MAX = 50
    USERNAME_LENGTH_MIN = 3
    USERNAME_LENGTH_MAX = 15
    PASSWORD_LENGTH_MIN = 6
    PASSWORD_LENGTH_MAX = 20

    email = StringField("Email", validators=[DataRequired(message="Enter an email address."),
                                             Length(max=EMAIL_LENGTH_MAX,
                                                    message=f"Email cannot be more than {EMAIL_LENGTH_MAX} characters long."),
                                             Email(message="Enter a valid email address.")])
    full_name = StringField("Full Name", validators=[DataRequired(message="Enter a full name."),
                                                     Length(max=FULL_NAME_LENGTH_MAX,
                                                            message=f"Full name cannot be more than {FULL_NAME_LENGTH_MAX} characters long.")])
    username = StringField("Username", validators=[DataRequired(message="Enter a username."),
                                                   AlphaNumeric(message="Username can only contain characters and numbers."),
                                                   Length(min=USERNAME_LENGTH_MIN, max=USERNAME_LENGTH_MAX,
                                                          message=f"Username must be {USERNAME_LENGTH_MIN} to {USERNAME_LENGTH_MAX} characters long.")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter a password."),
                                                     Length(min=PASSWORD_LENGTH_MIN, max=PASSWORD_LENGTH_MAX,
                                                            message=f"Password must be {PASSWORD_LENGTH_MIN} to {PASSWORD_LENGTH_MAX} characters long.")])
    sign_up = SubmitField("Sign Up")

    def validate_email(self, email):
        user = User.get_by_email(email.data)

        if user:
            raise ValidationError(f"Email {email.data} already exists.")

    def validate_username(self, username):
        user = User.get_by_username(username.data)

        if user:
            raise ValidationError(f"Username {username.data} already exists.")
