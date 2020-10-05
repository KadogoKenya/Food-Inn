from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime





class Giphy:
    '''
    Food class to define the Food obajects available.
    '''

    def __init__(self,id,url,title,images):

        self.id=id
        self.url=url
        self.title=title
        self.images=images


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    email = db.Column(db.String(255),unique = True,index = True)
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

# class comment(db.Model):    
    
#     id = db.Column(db.Integer, primary_key = True)
#     comment_post = db.Column(db.String(255), index=True)
#     time = db.Column(db.DateTime, default=datetime.utcnow)
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
#     def save_comments(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(cls, id):
#         comments = Comment.query.filter_by(post_id=id).all()
#         return comments
        