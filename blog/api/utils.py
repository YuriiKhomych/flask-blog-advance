from blog import db
from blog.posts.models import Post


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_all_posts():
    return Post.query.order_by(Post.created.desc()).all()


def create_new_post(data):
    post = Post(**data)
    save_changes(data=post)
