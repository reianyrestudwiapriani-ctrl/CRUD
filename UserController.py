from app.model.user import Users
from app import response, db
from flask import request

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        return response.badRequest([], str(e))


def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email
        })
    return array


def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'User not found')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        return response.badRequest([], str(e))


def singleTransform(users):
    return {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }


def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(name=name, email=email)
        users.setPassword(password)

        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Successfully created user!')
    except Exception as e:
        return response.badRequest([], str(e))


def update(id):
    try:
        users = Users.query.filter_by(id=id).first()

        if not users:
            return response.badRequest([], 'User not found')

        users.name = request.json['name']
        users.email = request.json['email']
        users.setPassword(request.json['password'])

        db.session.commit()

        return response.ok('', 'Successfully updated user!')
    except Exception as e:
        return response.badRequest([], str(e))


def delete(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'User not found')
        
        db.session.delete(users)
        db.session.commit()

        return response.ok('', 'Successfully deleted user!')
    except Exception as e:
        return response.badRequest([], str(e))
