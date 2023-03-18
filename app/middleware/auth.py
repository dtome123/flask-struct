import jwt
import config
from functools import wraps
from flask import request, jsonify, session, render_template
from app.dao.user import repository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if 'token' in session:
            token = session['token']

        # return 401 if token is not passed
        if not token:
            return jsonify({
                'message': 'missing token'
            }), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
            current_user = repository.get_by_id(data['id'])
        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated
