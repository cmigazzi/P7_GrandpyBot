"""Flask application factory."""

import os

from flask import Flask

# Get environment variables
G_API_KEY = os.environ.get("G_API_KEY")


def create_app(test_config=None):
    """Is factory function."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import index
    app.register_blueprint(index.bp)

    return app
