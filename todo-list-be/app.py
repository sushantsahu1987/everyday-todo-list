from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.todo import Todo, TodoList, TodoCreation
from resources.user import Login, Logout, Register, User

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "SECRET"

api = Api(app)
jwt = JWTManager(app)


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    return jsonify({"user_role": identity["role"], "user_id": identity["user_id"]})

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({"message": "Token has expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"message": "Invalid authorization header"}), 401


api.add_resource(Todo, "/todo/<int:todo_id>")
api.add_resource(TodoList, "/todos")
api.add_resource(TodoCreation, "/todo")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(Register, "/register")
api.add_resource(User, "/user/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
