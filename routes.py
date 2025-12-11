from flask import request
from app.controller import UserController

def register_routes(app):

    @app.route('/users', methods=['GET', 'POST'])
    def user():
        if request.method == 'GET':
            return UserController.index()
        else:
            return UserController.store()

    @app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def user_detail(id):
        if request.method == 'GET':
            return UserController.show(id)
        elif request.method == 'PUT':
            return UserController.update(id)
        elif request.method == 'DELETE':
            return UserController.delete(id)
