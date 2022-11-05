import os
import pytest
from flaskr.app import create_app


@pytest.fixture()
def app():
    os.environ["DATABASE_URI"] = "sqlite:///:memory:"
    app = create_app("sqlite:///:memory:")
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
