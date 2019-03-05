"""Flask application factory."""

import os

from flask import Flask

# Get environment variables
G_API_KEY = os.environ.get("G_API_KEY")


def create_app():
    """Is factory function."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    from . import index
    app.register_blueprint(index.bp)

    return app
