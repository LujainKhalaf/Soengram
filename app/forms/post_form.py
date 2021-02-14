from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class PostForm(FlaskForm):
    post_image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

    description = StringField("Caption", widget=TextArea(), validators=[
        DataRequired(message="Caption Required"),
    ])

    submit = SubmitField("Create a Post")
