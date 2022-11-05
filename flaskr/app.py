"""Flask app entry file."""
from os import environ
import logging
from flask import Flask
from flaskr.routes import routes_blueprint
from flaskr.config import db


FLASK_DEBUG = environ.get("FLASK_DEBUG", False)
DEFAULT_DB_URI = "postgresql://dev_user:dev_user@host.docker.internal:5432/dev_database"


def create_app(database_uri=DEFAULT_DB_URI):
    app = Flask(__name__)
    app.register_blueprint(routes_blueprint, url_prefix="/")

    logging.debug("Provided database_uri: %s", database_uri)
    logging.debug(
        "Evaluated database_uri: %s", environ.get("DATABASE_URI", database_uri)
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URI", database_uri)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "secret string"

    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if FLASK_DEBUG else logging.INFO)
    app = create_app()
    app.run()
