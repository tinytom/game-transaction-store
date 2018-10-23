from flask import Flask
from flask_restplus import Api
from sqlalchemy import create_engine

from config import DevelopmentConfig


def configure_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    return app


app = configure_app()

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

api = Api()
api.init_app(app)
