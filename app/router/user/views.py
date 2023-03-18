from . import page
from flask import render_template, jsonify, request
from app.controller.user import get_me, create_user
from app.middleware.auth import token_required


@page.route('/user')
@token_required
def index(current_user):
    res = get_me.handle(current_user.id)
    return render_template('user/index.html', user=res)


@page.route('/user/create')
def create_view():
    return render_template('user/create.html')


@page.route('/user/create', methods=['POST'])
def create():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    role = 'user'

    res = create_user.handle(name, "", username, password, role)
    return render_template('user/index.html', user=res)
