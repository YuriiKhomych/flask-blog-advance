from flask import Flask

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from blog.config import Configuration

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    db.init_app(app)

    from blog.main.view import main
    from blog.posts.view import posts

    app.register_blueprint(main)
    app.register_blueprint(posts, url_prefix='/blog')

    ### ADMIN ###
    from blog.posts.models import Post, Tag

    admin = Admin(app)
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Tag, db.session))

    return app
