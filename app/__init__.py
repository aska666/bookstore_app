from flask import Flask
from config import Config
from .seed import initialize_data, reset_database
from .database import db
from .routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(main)

    with app.app_context():
        reset_database()
        initialize_data()

    return app
