from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='title field cannot be blank');

class Todo(Resource):

    def get(self, todo_id):
        return {'message': "you get a todo item with {}".format(todo_id)};

    def put(self, todo_id):
        return {'message': "you can now update todo item with {}".format(todo_id)};



class TodoList(Resource):

    def get(self):
        return {'message': 'list of todos'}


class TodoCreation(Resource):

    def post(self):
        data = parser.parse_args()
        # print(data)
        return {'message': "{} is added to the list".format(data.title)}