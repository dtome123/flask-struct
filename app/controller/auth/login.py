import jwt
import config
from app.dao.user import repository, model
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from flask import session


exp = 30 * 24 * 60 * 60


def handle(username, password):
    try:
        user = repository.get_by_username(username)
        if user and check_password_hash(user.password, password):
            token = jwt.encode({
                'id': user.id,
                'exp': datetime.utcnow() + timedelta(seconds=exp),
            }, config.SECRET_KEY, algorithm='HS256')

            session['token'] = token
            return token
        return None
    except Exception as e:
        print("error:", e)
        return None
