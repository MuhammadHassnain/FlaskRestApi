
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'MY LITTLE SECRET KEY'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    server = 'localhost'
    password = 'password'
    database = 'RBA'
    user = 'root'
    ERROR_INCLUDE_MESSAGE = False
    SQLALCHEMY_DATABASE_URI = f"mysql://{user}:{password}@{server}:3306/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig()
)

key = Config.SECRET_KEY
