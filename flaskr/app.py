from os import environ
from flask import Flask

from flaskr.routes import routes_blueprint
from flaskr import db


def create_app(database_uri='postgresql://dev_user:dev_user@localhost:5432/dev_database'):
    app = Flask(__name__)
    
    app.register_blueprint(routes_blueprint, url_prefix='/')

    print(database_uri)
    print(environ.get('DATABASE_URI', database_uri))
    app.config['SQLALCHEMY_DATABASE_URI'] =  environ.get('DATABASE_URI', database_uri)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = 'secret string'

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()

    app.run()