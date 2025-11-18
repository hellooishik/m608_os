from flask import Blueprint, request, jsonify
from .models import User
from .schemas import RegisterSchema
from flask_jwt_extended import create_access_token
from .utils import hash_password, verify_password

auth_bp = Blueprint("auth", __name__)
schema = RegisterSchema()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return {"errors": errors}, 400
    if User.objects(username=data["username"]).first():
        return {"message": "username exists"}, 400
    user = User(username=data["username"], password_hash=hash_password(data["password"]))
    user.save()
    return {"message": "user created"}, 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.objects(username=data.get("username")).first()
    if not user or not verify_password(user.password_hash, data.get("password")):
        return {"message": "invalid credentials"}, 401
    token = create_access_token(identity=str(user.id))
    return {"access_token": token}, 200
