from . import page
from flask import render_template, request, redirect
from app.controller.auth import login as login_controller
from app.controller.user import create_user


@page.route('/login')
def index():
    return render_template('login/index.html', title="Welcome")


@page.route('/login', methods=['POST'])
def login():
    token = login_controller.handle(
        request.form['username'], request.form['password'])

    if token:
        return redirect('/user')
    else:
        return render_template('login/index.html', title="Login",
                               message="Invalid Credentials")
