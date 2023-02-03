# Imports
from flask import Flask, request
from flask_restx import Api, Resource, abort, reqparse
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


# Start flask app
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Parser
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='provide name as str', required=True)
video_put_args.add_argument('likes', type=int, help='provide number of likes as int', required=True)
video_put_args.add_argument('views', type=int, help='provide number of views as int', required=True)


# Models
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


# with app.app_context():
#    db.create_all()  # DO THIS ONLY ONCE


# Create Marshmallow Schema
class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VideoModel
video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)


# Resources
class Video(Resource):

    def get(self, video_id):  # gets a resource
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, kwargs={'msg': 'Could not find video with this id...'})
        return video_schema.jsonify(result)

    @api.expect(video_put_args, validate=True)
    def post(self, video_id):  # creates or replaces a resource
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, kwargs={'msg': 'video_id already in use...'})

        video = VideoModel(id=video_id, name=request.json['name'],
                           views=request.json['views'], likes=request.json['likes'])
        db.session.add(video)
        db.session.commit()
        return {'msg': 'successfully created video'}, 201

    @api.expect(video_put_args, validate=True)
    @api.doc(responses={200: 'Success', 404: 'Not Found' })
    def patch(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, kwargs={'msg': 'video_id not found...'})

        result.name = request.json['name']
        result.views = request.json['views']
        result.likes = request.json['likes']

        db.session.commit()

        return {'msg': 'successfully updated video'}, 200

    @staticmethod
    def delete(video_id):  # deletes a resource
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, kwargs={'msg': 'Could not find video with this id...'})

        VideoModel.query.filter_by(id=video_id).delete()
        db.session.commit()
        return {'msg': 'deleted'}, 204


api.add_resource(Video, "/video/<int:video_id>")

# Main
if __name__ == '__main__':
    app.run(debug=True)
