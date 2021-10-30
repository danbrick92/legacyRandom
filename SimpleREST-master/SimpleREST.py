from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app, prefix="/api/test")
data = {"meaning_of_life": 42}
auth = HTTPBasicAuth()
fakeUser = { "dan" : "123"}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return fakeUser.get(username) == password

class PrivateResource(Resource):
    @auth.login_required

    @app.route('/private')
    def get(self):
        global data
        return data

    @app.route('/private', methods=['POST'])
    def post(self):
        global data
        data['id'] = request.get_json()
        return '',204

    @app.route('/private', methods=['DELETE'])
    def delete(self):
        global data
        data['id'] = ""
        return '', 204

api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)