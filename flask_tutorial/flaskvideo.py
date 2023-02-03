# Imports
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
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


# Data
people = {
    'dan': {'age': 30, 'gender': 'male'},
    'cheryl': {'age': 28, 'gender': 'female'}
}

videos = {

}

# Parsers
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='provide name as str', required=True)
video_put_args.add_argument('likes', type=int, help='provide number of likes as int', required=True)
video_put_args.add_argument('views', type=int, help='provide number of views as int', required=True)


# Resources
class HelloWorld(Resource):
    @staticmethod
    def get(name: str):
        return people[name]
    #
    # @staticmethod
    # def post():
    #     return {"data": "Posted"}


class Video(Resource):
    def get(self, video_id):  # gets a resource
        self.abort_if_not_found(video_id)
        return videos[video_id]

    def post(self, video_id):  # creates a resource
        self.abort_if_found(video_id)
        return self.put(video_id)

    @staticmethod
    def put(video_id):  # creates or replaces a resource
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):  # deletes a resource
        self.abort_if_not_found(video_id)
        del videos[video_id]
        return {'msg': 'deleted'}, 204

    @staticmethod
    def abort_if_not_found(video_id):
        if video_id not in videos:
            abort(404, kwargs={'message': "video_id not found..."})

    @staticmethod
    def abort_if_found(video_id):
        if video_id in videos:
            abort(409, kwargs={'message': "video_id already exists..."})


api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")

# Main
if __name__ == '__main__':
    app.run(debug=True)
