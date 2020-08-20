from flask_restful import Resource, reqparse

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email', required=True, help="email field cannot be blank")
_user_parser.add_argument('password', required=True, help="email field cannot be blank")
_user_parser.add_argument("Client-Key", required=True, location='headers', help="Client-Key header cannot be emtpy")

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
        return {
            "message": "logged in successfully with {} and {}".format(
                data.email, data.password
            )
        }


class Logout(Resource):
    def post(self):
        return {"message": "logged out successfully!"}


class Register(Resource):
    def post(self):
        data = _user_parser.parse_args()
        return {"message": "{} is registered successfully!".format(data.email)}


class User(Resource):
    def get(self, user_id):
        return {"message": "User with id {}".format(user_id)}

    def put(self, user_id):
        data = _user_update_parser.parse_args()
        return {
            "message": "Update user with email, id, password, new_password {} {} {} {} ".format(
                data.email, user_id, data.password, data.new_password
            )
        }

