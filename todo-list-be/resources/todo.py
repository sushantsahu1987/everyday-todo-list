from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='title field cannot be blank');

class Todo(Resource):
    @jwt_required
    def get(self, todo_id):
        return {'message': "you get a todo item with {}".format(todo_id)};

    @jwt_required
    def put(self, todo_id):
        return {'message': "you can now update todo item with {}".format(todo_id)};



class TodoList(Resource):
    @jwt_required
    def get(self):
        return {'message': 'list of todos'}


class TodoCreation(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()
        # print(data)
        return {'message': "{} is added to the list".format(data.title)}