from flask import Blueprint

page = Blueprint('login', __name__)

from . import views