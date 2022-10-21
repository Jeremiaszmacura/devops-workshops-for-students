from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] =  environ.get('DATABASE_URI', 'postgresql://dev_user:dev_user@localhost:5432/dev_database')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = 'secret string'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

app = create_app()

import flaskr.models
import flaskr.routes

app.run()