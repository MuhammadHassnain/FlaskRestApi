
from flask_restx import Resource
from flask_restx import Namespace
from app.main import db
import pandas as pd

home = Namespace('home', description='Homw Namespace')


@home.route('/')
class Index(Resource):

    def get(self):
        print('Hello world!')
        result = db.session.execute('SELECT * FROM user')
        df = pd.DataFrame(result, columns=result.keys())
        print(df)
        return 'Welcome to the Home'
