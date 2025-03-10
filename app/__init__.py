from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    from app.models.board import Board
    from app.models.card import Card

    db.init_app(app)
    migrate.init_app(app, db)
    from app.routes.board import board_bp
    from app.routes.card import card_bp
    
    app.register_blueprint(board_bp)
    app.register_blueprint(card_bp)

    CORS(app)
    return app

