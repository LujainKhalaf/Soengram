from app.models import Comment


def create_mock_comment() -> Comment:
    return Comment(comment_id=1, user_id=1, post_id=1, comment_text="comment text")
