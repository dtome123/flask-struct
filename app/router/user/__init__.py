from flask import Blueprint

page = Blueprint('user', __name__)

from . import views