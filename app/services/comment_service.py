from flask import jsonify

from app.forms.comment_form import AddCommentForm
from app.models import Comment, Post
from app.utils.entities import JSONResponse
from datetime import datetime


def add_comment(user_id: int, form: AddCommentForm) -> JSONResponse:
    post_id = form.post_id.data
    post = Post.get_by_post_id(post_id)
    if post:
        comment = comment_builder(user_id, form)

        Comment.insert(comment)
        return comment, 200
    return None, 404


def delete_comment(user_id: int, comment_id: int) -> JSONResponse:
    comment = Comment.get_by_comment_id(comment_id)

    if not Comment.is_comment_owned_by_user(comment, user_id):
        return jsonify('Comment not found'), 404

    Comment.delete(comment)

    return jsonify('Comment deleted'), 204


def comment_builder(user_id: int, form: AddCommentForm) -> Comment:
    return Comment(
        user_id=user_id,
        post_id=form.post_id.data,
        comment_text=form.comment.data,
        created_at=datetime.now()
    )
