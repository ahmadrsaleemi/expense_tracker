from flask import Blueprint
from .expenses import expenses_bp
from .upload import upload_bp
from .auth import auth_bp

def register_routes(app):
    app.register_blueprint(expenses_bp, url_prefix="/api/v1/expenses")
    app.register_blueprint(upload_bp, url_prefix="/api/v1/upload")
    app.register_blueprint(auth_bp, url_prefix="/api/v1/")