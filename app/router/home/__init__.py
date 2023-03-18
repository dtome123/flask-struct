from flask import Blueprint

page = Blueprint('home', __name__)

from . import views