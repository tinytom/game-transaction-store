from flask import Flask
from flask_restplus import Api
from config import DevelopmentConfig
from sqlalchemy import create_engine


def configure_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    return app


app = configure_app()

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

api = Api()
api.init_app(app)
