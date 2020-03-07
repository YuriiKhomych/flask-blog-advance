from flask import Flask

from blog.config import Configuration
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    db.init_app(app)

    from blog.main.view import main
    from blog.posts.view import posts

    app.register_blueprint(main)
    app.register_blueprint(posts, url_prefix='/blog')

    return app
