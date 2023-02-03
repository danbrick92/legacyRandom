# Imports
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


# Start flask app
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


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


# Parsers
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='provide name as str', required=True)
video_put_args.add_argument('likes', type=int, help='provide number of likes as int', required=True)
video_put_args.add_argument('views', type=int, help='provide number of views as int', required=True)


# Fields
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


# Resources
class Video(Resource):

    @marshal_with(resource_fields)
    def get(self, video_id):  # gets a resource
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, kwargs={'msg': 'Could not find video with this id...'})
        return result

    @marshal_with(resource_fields)
    def post(self, video_id):  # creates or replaces a resource
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, kwargs={'msg': 'video_id already in use...'})

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_put_args.parse_args()  # would leave out all the required normally, here we won't
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, kwargs={'msg': 'video_id not found...'})

        result.name = args['name']
        result.views = args['views']
        result.likes = args['likes']

        db.session.commit()

        return result, 200

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
