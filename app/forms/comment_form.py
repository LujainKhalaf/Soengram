from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, HiddenField, StringField
from wtforms.validators import DataRequired, Length


class AddCommentForm(FlaskForm):
    COMMENT_LENGTH_MAX = 2_200

    post_id = HiddenField(
        validators=[
            DataRequired()
        ]
    )
    comment = TextAreaField(
        'Add a Comment...',
        render_kw={'rows': 1, 'style': 'height: auto'},
        validators=[
            DataRequired(message='Comment Required'),
            Length(
                max=COMMENT_LENGTH_MAX,
                message=f"Comment cannot be more than {COMMENT_LENGTH_MAX} characters long."
            )
        ]
    )
    component = StringField('Component')

    submit = SubmitField("Post")
