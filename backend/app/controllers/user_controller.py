from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService

user_ns = Namespace("users", "Users operations")

user_model = user_ns.model(
    "User", {"id": fields.Integer(readonly=True), "name": fields.String(readonly=True)}
)


@user_ns.route("/")
class UserList(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        return UserService.get_all_users()
    
    @user_ns.marshal_with(user_model, code=201)
    @user_ns.expect(user_model, validate=True)
    def post(self):
        """Create a user"""
        return UserService.create_user(user_ns.payload), 201