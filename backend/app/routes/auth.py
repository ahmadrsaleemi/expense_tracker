from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_service import UserService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing username, email or password"}), 400
    
    user, error = UserService.create_user(username, email, password)

    if error:
        return jsonify({"error": error}), 409
    
    return jsonify({
        "success" : True,
        "message" : "User created successfully",
        "user" : {
            "username" : user.username,
            "email" : user.email
        }
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = UserService.get_by_email(email)

    if not user or not user.verify_password(password):
        return jsonify({"error" : "Invalid email/password credentials"}), 401
    
    access_token = create_access_token(identity = user.id)
    return jsonify({"access_token" : access_token}), 200