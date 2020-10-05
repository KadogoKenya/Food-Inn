from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Giphy:
    '''
    Food class to define the Food obajects available.
    '''

    def __init__(self,id,url,title,images):

        self.id=id
        self.url=url
        self.title=title
        self.images=images


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    

    def __repr__(self):
        return f'User {self.name}'
        comment = db.Column(db.Text(),nullable = False)
        users = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
        role_id = db.Column(db.Integer,db.ForeignKey('roles.id'),nullable = False)