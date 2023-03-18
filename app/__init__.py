import os
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    

    app.app_context().push()
    db.init_app(app)
    Session(app)

    from app.router import login, home, user

    app.register_blueprint(home.page)
    app.register_blueprint(login.page)
    app.register_blueprint(user.page)

    return app
