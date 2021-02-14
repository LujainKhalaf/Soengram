from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)


class PostForm(FlaskForm):
    post_image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')])
    description = StringField("Caption", validators=[
        DataRequired(message="Caption Required"),
    ])
    submit_buttn = SubmitField("Create a Post")
