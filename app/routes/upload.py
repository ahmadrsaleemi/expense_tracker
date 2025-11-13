import os
from flask import Blueprint, request, jsonify

from app.controllers.upload_controller import save_file, send_to_queue

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/", methods=["POST"])
def file_upload():
    if "file" not in request.files:
        return jsonify({"error": "No file found"}), 400
    

    file = request.files["file"]

    file_path, error = save_file(file)

    try:
        send_to_queue(os.path.basename(file_path))
    except Exception as e:
        return jsonify({"error": f"Failed to queue task: {str(e)}"}), 500

    if error:
        return jsonify({"error": error}), 400
    
    return jsonify({"message": "File uploaded successfully!", "file_path" : file_path}), 201