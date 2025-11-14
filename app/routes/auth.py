from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    fullname = data.get("fullname")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password or not fullname:
        return jsonify({"error": "Missing username, email, password or fullname"}), 400
    
    user, error = UserService.create_user(username, email, password, fullname)

    if error:
        return jsonify({"error": error}), 409
    
    return jsonify({
        "message" : "User created successfully",
        "user" : {
            "username" : user.username,
            "email" : user.email
        }
    }), 201