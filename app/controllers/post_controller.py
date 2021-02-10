import uuid
from flask import request, Blueprint, render_template, redirect, url_for, flash
from app.services import post_service
from app.utils.session_decorators import session_required
from app.utils.validation import is_post_image_valid
from app.utils.file import get_file_extension, get_image_url


post_routes = Blueprint('post_routes', __name__)


@post_routes.route('/post', methods=['GET', 'POST'])
@session_required
def create_post(user_id):
    if request.method == 'GET':
        return render_template('create_post.html', message='Hello World!')

    if request.method == 'POST':
        description = request.form.get('description')

        if is_post_image_valid(request.files):
            flash('A valid image is required to make a post')
            return redirect(request.url)

        file = request.files['post_image']
        filename = f'{uuid.uuid1().hex}.{get_file_extension(file.filename)}'
        image_url = get_image_url(filename)

        post_service.create_post(user_id, image_url, description)
        post_service.upload_post_image(file, image_url)

        return redirect(url_for("index_routes.index"))
