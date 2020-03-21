from flask import request

from api.utils import get_all_posts, create_new_post
from flask_restplus import fields, Resource, Namespace


api = Namespace('posts_api', description='Posts', path='/api')

post_model = api.model('post', {
    'title': fields.String(readonly=True, description='Title of post'),
    'body': fields.String(required=True, description='Body of post'),
})


@api.route('/posts')
class PostListResource(Resource):
    '''Shows a list of all posts, and lets you POST to add new post'''
    @api.doc('list_posts')
    @api.marshal_list_with(post_model, envelope='data')
    def get(self):
        '''List all posts'''
        return get_all_posts()

    @api.doc('create_post')
    @api.expect(post_model)
    @api.marshal_with(post_model, code=201)
    def post(self):
        '''Create a new post'''
        data = request.json
        post = create_new_post(data=data)
        return post, 201
