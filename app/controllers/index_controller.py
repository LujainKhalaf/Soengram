from flask import request, Blueprint, render_template

from app.utils.session_decorators import login_required

index_routes = Blueprint('index_routes', __name__)


@index_routes.route('/', methods=['GET'])
@login_required
def index(_):
    if request.method == 'GET':
        return render_template('base.html', message='Hello World!')
