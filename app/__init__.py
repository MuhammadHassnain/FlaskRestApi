from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint
from flask_restx import Api
from app.config import config_by_name
from app.home.views import home as home_ns


db = SQLAlchemy()


blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Flask Rest Api Sample', version='1.0',
          description='A tempelate for Flask Rest Api')

api.add_namespace(home_ns, '/home')


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    app.register_blueprint(blueprint)
    app.app_context().push()
    return app
