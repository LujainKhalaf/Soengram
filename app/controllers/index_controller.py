from flask import request, Blueprint, render_template, session

index_routes = Blueprint('index_routes', __name__)


@index_routes.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('base.html', message='Hello World!')
