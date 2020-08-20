from flask import Flask, jsonify
from flask_restful import Api
from resources.todo import Todo, TodoList, TodoCreation
from resources.user import Login, Logout, Register, User

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, '/todo/<int:todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(TodoCreation, '/todo')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Register, '/register')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)