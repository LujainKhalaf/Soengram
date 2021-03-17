from typing import Any
from flask import request, Blueprint, render_template
from app.services import comment_service
from app.utils.session import login_required
from app.forms.comment_form import AddCommentForm


comment_routes = Blueprint('comment_routes', __name__)


@comment_routes.route('/add-comment', methods=['POST'])
@login_required
def add_comment(user_id: int) -> Any:
    form = AddCommentForm()

    comment, status_code = comment_service.add_comment(user_id, form)

    if comment:
        template = render_template(
            'components/post/_post_comment.html',
            user=comment.user,
            comment=comment,
            commentType='userComment',
            postDisplayType='card'
        )
        return template

    return status_code


@comment_routes.route('/delete-comment', methods=['DELETE'])
@login_required
def delete_comment(user_id: int) -> Any:
    comment_id = request.form.get('comment_id')
    return comment_service.delete_comment(user_id, comment_id)
