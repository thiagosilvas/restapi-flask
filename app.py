from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    "port": 27017,
    'host': 'mongodb',
    "username": "admin",
    "password": "admin"
}

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name', type=str, required=True, help="Não pode ser vazio")
_user_parser.add_argument('last_name', type=str, required=True, help="Não pode ser vazio")
_user_parser.add_argument('email', type=str, required=True, help="Não pode ser vazio")
_user_parser.add_argument('cpf', type=str, required=True, help="Não pode ser vazio")
_user_parser.add_argument('birth_date', type=str, required=True, help="Não pod ser vazio")

api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)

class User(Resource):
    def get(self):
        return {'message': 'user 1'}
    def post(self):
        data = _user_parser.parse_args()
        UserModel(**data).save()
    
class Users(Resource):
    def get(self):
        return {'message': 'all users'}    

api.add_resource(User, '/user', '/user/<string>:cpf')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")