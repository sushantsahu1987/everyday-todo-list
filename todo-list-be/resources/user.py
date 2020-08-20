from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_claims,
)

_user_parser = reqparse.RequestParser()
_user_parser.add_argument("email", required=True, help="email field cannot be blank")
_user_parser.add_argument("password", required=True, help="email field cannot be blank")
_user_parser.add_argument(
    "Client-Key",
    required=True,
    location="headers",
    help="Client-Key header cannot be emtpy",
)

_user_update_parser = reqparse.RequestParser()
_user_update_parser.add_argument(
    "email", required=True, help="email field cannot be blank"
)
_user_update_parser.add_argument(
    "password", required=True, help="password cannot be empty"
)
_user_update_parser.add_argument(
    "new_password", required=True, help="new password cannot be empty"
)


class Login(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = {"user_id": 1, "role": "admin"}
        access_token = create_access_token(identity=user, fresh=True)
        refresh_token = create_refresh_token(identity=user)
        return {
            "message": "logged in successfully with {}".format(data.email),
            "access_token": access_token,
            "refresh_token": refresh_token,
        }


class Logout(Resource):
    @jwt_required
    def post(self):
        return {"message": "logged out successfully!"}


class Register(Resource):
    def post(self):
        data = _user_parser.parse_args()
        return {"message": "{} is registered successfully!".format(data.email)}


class User(Resource):
    @jwt_required
    def get(self, user_id):
        data = get_jwt_claims()
        print(data)
        return {"message": "User with id {}".format(user_id)}

    @jwt_required
    def put(self, user_id):
        data = _user_update_parser.parse_args()
        return {
            "message": "Update user with email, id, password, new_password {} {} {} {} ".format(
                data.email, user_id, data.password, data.new_password
            )
        }

