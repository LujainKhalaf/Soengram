from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from app.models import User


class SigninForm(FlaskForm):
    EMAIL_LENGTH_MAX = 50
    PASSWORD_LENGTH_MIN = 6
    PASSWORD_LENGTH_MAX = 20

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Enter an email address."),
            Length(max=EMAIL_LENGTH_MAX, message=f"Email cannot be more than {EMAIL_LENGTH_MAX} characters long."),
            Email(message="Enter a valid email address.")
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Enter a password."),
            Length(
                min=PASSWORD_LENGTH_MIN,
                max=PASSWORD_LENGTH_MAX,
                message=f"Password must be {PASSWORD_LENGTH_MIN} to {PASSWORD_LENGTH_MAX} characters long."
            )
        ]
    )

    sign_in = SubmitField("Sign In")

    def validate(self) -> bool:
        if not super().validate():
            return False

        user = User.get_by_email(self.email.data)

        if not User.is_authenticated(user, self.password.data):
            self.email.errors.append('Incorrect username and/or password.')
            return False

        return True
