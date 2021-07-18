
from flask_restx import Resource
from . import home


@home.route('/')
class Index(Resource):

    def get(self):
        return 'Welcome to the Home'
