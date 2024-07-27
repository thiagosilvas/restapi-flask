from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        return {'message': 'user 1'}
    def post(self, cpf):
        return {'message': cpf}

    
class Users(Resource):
    def get(self):
        return {'message': 'all users'}    

api.add_resource(User, '/user', '/user/<string>:cpf')
api.add_resource(Users, '/users')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")