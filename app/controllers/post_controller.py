import os
import uuid
from flask import request, Blueprint, render_template, redirect, url_for, flash
from app.utils.session_decorators import session_required
from app.utils.validation import is_post_image_valid
from app.utils.file import get_file_extension, get_post_images_dir


post_routes = Blueprint('post_routes', __name__)


@post_routes.route('/post', methods=['GET', 'POST'])
@session_required
def create_post(user_id):
    if request.method == 'GET':
        return render_template('create_post.html', message='Hello World!')

    if request.method == 'POST':
        if is_post_image_valid(request.files):
            flash('A valid image is required to make a post')
            return redirect(request.url)

        file = request.files['post_image']
        filename = f'{uuid.uuid1().hex}.{get_file_extension(file.filename)}'
        file.save(os.path.join(get_post_images_dir(), filename))

        return redirect(url_for("index_routes.index"))
