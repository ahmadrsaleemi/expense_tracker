from flask import Blueprint
from .expenses import expenses_bp

def register_routes(app):
    app.register_blueprint(expenses_bp, url_prefix="/api/v1/expenses")