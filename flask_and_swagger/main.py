# Imports
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, jsonify
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create Flask App
app = Flask(__name__)


# Return default home message
@app.route('/')
def hello_world():
    return "Hello World!"


# Create Flask API Spec
spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)


# Define what happens when we try to get the API spec
@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())


# Declare response format for each to do item
class TodoResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    status = fields.Boolean()


# Declare response format for the whole to do list
class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoResponseSchema))


# Create GET response
@app.route('/todo')
def todo():
    """
    Get List of Todo
        ---
        get:
            description:  get list of todos
            response:
                200:
                    description: return a todo list
                    content:
                        application/json:
                            schema: TodoListResponseSchema
    """
    dummy_data = [
        {
            "id": 1,
            "task": "finish this task",
            "status": False
        },
        {
            "id": 2,
            "task": "finish old task",
            "status": True
        }
    ]
    return TodoListResponseSchema().dump({'todo_list': dummy_data})


# Register the GET API
with app.test_request_context():
    spec.path(view=todo)


if __name__ == '__main__':
    app.run(debug=True)
