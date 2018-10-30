from flask import Blueprint

# This instance represents the authentication blueprint
auth_blueprint = Blueprint('auth', __name__)

from . import views
