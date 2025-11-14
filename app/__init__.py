import os 
from flask import Flask
from app.extensions import db, migrate

from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    #i will fix this later as well
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@postgres:5432/expense_db"
    )

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    # Register routes AFTER models and db init
    from app.routes import register_routes
    register_routes(app)

    return app