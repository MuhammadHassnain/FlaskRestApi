from flask import Blueprint
from flask_restx import Api
from app.main.api.home.views import home as home_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Flask Rest Api Sample', version='1.0',
          description='A tempelate for Flask Rest Api')

api.add_namespace(home_ns, '/home')
