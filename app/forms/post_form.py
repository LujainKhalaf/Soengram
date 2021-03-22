from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

from app.utils.file import ALLOWED_EXTENSIONS


class CreatePostForm(FlaskForm):
    DESCRIPTION_LENGTH_MAX = 2_200

    post_image = FileField(
        "Image",
        render_kw={
            "style": "height: auto",
            "onchange": "previewImage(event)",
            "accept": "image/*",
        },
        validators=[
            FileRequired(message="Must attach a photo"),
            FileAllowed(ALLOWED_EXTENSIONS, "File type not allowed"),
        ],
    )

    description = TextAreaField(
        "Caption",
        render_kw={"rows": 5, "style": "height: 100%"},
        validators=[
            DataRequired(message="Caption Required"),
            Length(
                max=DESCRIPTION_LENGTH_MAX,
                message=f"Caption cannot be more than {DESCRIPTION_LENGTH_MAX} characters long.",
            ),
        ],
    )

    submit = SubmitField("Upload")
