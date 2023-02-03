# Imports
import flask
from flask import Flask, request
from flask_restx import Api, Resource, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


# Start flask app
app = Flask(__name__)
api = Api(app, title='Swords', description='Add, remove, or get a sword in your inventory')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dan.db"
app.config['JWT_SECRET_KEY'] = 'super-secret'  # really important to secure this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 5  # expires after 5 seconds
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


# Create model
class SwordModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, doc='sword id')
    name = db.Column(db.String(50), nullable=False, doc='sword name')
    style = db.Column(db.String(50), nullable=False, doc='sword style')
    year = db.Column(db.Integer, nullable=False, doc='sword year forged')

    def __repr__(self):
        print(f"Sword(id={self.id}, name={self.name}, style={self.style}, year={self.year})")


# Create schema
class SwordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SwordModel


sword_schema = SwordSchema()
swords_schema = SwordSchema(many=True)


# Classes
class Sword(Resource):

    @staticmethod
    def check_sword_id_found(sword_id: int, is_post: bool):
        sword = db.session.get(SwordModel, sword_id)
        if is_post and sword:
            abort(409, kwargs={'msg': 'sword_id already in use...'})
        elif not is_post and not sword:
            abort(404, kwargs={'msg': 'sword_id not found...'})
        return sword

    @api.doc(responses={200: "Success", 404: "Couldn't find sword"})
    def get(self, sword_id: int):
        """
        Get a sword from your inventory.
        """
        sword = self.check_sword_id_found(sword_id, False)
        return sword_schema.jsonify(sword)

    @api.doc(responses={200: "Success", 400: "Bad parameters", 409: "Sword already exists"},
             params={'name': SwordModel.name.doc, 'style': SwordModel.style.doc, 'year': SwordModel.year.doc})
    def post(self, sword_id: int):
        """
        Save a sword to your inventory.
        """
        _ = self.check_sword_id_found(sword_id, True)
        errors = sword_schema.validate(request.json)
        if errors:
            abort(400, kwargs={'msg': f'invalid parameters specified with errors:{errors}...'})

        sword = SwordModel(id=sword_id, name=request.json.get('name'), style=request.json.get('style'),
                           year=request.json.get('year'))
        db.session.add(sword)
        db.session.commit()
        return sword_schema.jsonify(sword)

    @api.doc(responses={200: "Success", 404: "Couldn't find sword"})
    def delete(self, sword_id):
        """
        Remove a sword from your inventory.
        """
        sword = self.check_sword_id_found(sword_id, False)
        db.session.delete(sword)
        db.session.commit()
        return {'msg': 'deleted'}


# Authentication
class Login(Resource):
    put_group = [1, 3, 5]
    both_group = [2, 4, 6]

    def get(self, login_id):
        login_id = create_access_token(identity=login_id)
        return flask.jsonify(token=login_id)

    @jwt_required()
    def post(self, login_id):
        current_user = get_jwt_identity()
        if current_user in self.both_group:
            message = 'success'
        else:
            abort(401, kwargs={'msg': 'not authorized'})
        return flask.jsonify(message=message, current_user=current_user)

    @jwt_required()
    def put(self, login_id):
        current_user = get_jwt_identity()
        if current_user in self.put_group or current_user in self.both_group:
            message = 'success'
        else:
            abort(401, kwargs={'msg': 'not authorized'})
        return flask.jsonify(message, current_user=current_user)


# Final Steps
# with app.app_context():
#     db.create_all()  # DO THIS ONLY ONCE
api.add_resource(Sword, "/sword/<int:sword_id>")
api.add_resource(Login, "/login/<int:login_id>")

# Main
if __name__ == '__main__':
    app.run(debug=True)
