from flask import Flask
from .config import Config
from flask_jwt_extended import JWTManager
from mongoengine import connect

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    connect(
        db=app.config["MONGO_DB_NAME"],
        host=app.config["MONGO_URI"]
    )

    jwt.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
