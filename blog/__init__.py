from flask import Flask

from flask_admin import Admin
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

from blog.config import Configuration

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)

    db.init_app(app)

    from blog.errors.view import errors
    from blog.main.view import main
    from blog.posts.view import posts

    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(posts, url_prefix='/blog')

    ### ADMIN ###
    from blog.posts.models import Post, Tag
    from blog.admin.view import HomeAdminView, PostAdminView, TagAdminView
    admin = Admin(
        app,
        'FlaskApp',
        url='/',
        index_view=HomeAdminView(name='Home')
    )
    admin.add_view(PostAdminView(Post, db.session))
    admin.add_view(TagAdminView(Tag, db.session))

    ### Flask-security ###
    from blog.admin.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    return app
