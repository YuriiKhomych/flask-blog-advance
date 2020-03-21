from flask import Blueprint
from flask_restplus import Api

from api.views import api as posts_namespace

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    api_blueprint,
    version='1.0',
    title='Posts API',
    description='A simple Posts API',
)
api.add_namespace(posts_namespace)
