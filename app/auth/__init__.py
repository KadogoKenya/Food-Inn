from flask import Blueprint
# from .auth import auth as auth_blueprint

# from . import views,forms

auth = Blueprint('auth',__name__)

from . import views,forms