import logging
from os import environ
from app import create_app, FLASK_DEBUG


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if FLASK_DEBUG else logging.INFO)
    app = create_app()
    app.run()
