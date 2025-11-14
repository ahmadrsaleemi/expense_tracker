from flask import Blueprint, jsonify, request

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/", methods=["GET"])
def get_expenses():
    return jsonify({"expenses": []})


@expenses_bp.route("/", methods=["POST"])
def add_expense():
    data = request.get_json()

    return jsonify({"message": "Expense Added!", "data": data}), 201