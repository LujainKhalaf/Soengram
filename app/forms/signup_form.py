from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignupForm(FlaskForm):

    email = StringField("Email", validators=[])
    full_name = StringField("Full Name", validators=[])
    username = StringField("Username", validators=[])
    password = PasswordField("Password", validators=[])
    sign_up = SubmitField("Sign Up")

