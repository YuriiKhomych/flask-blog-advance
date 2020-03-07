from flask import Flask

from blog.config import Configuration


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    return app
