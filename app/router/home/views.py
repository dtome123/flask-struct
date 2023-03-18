from . import page
from flask import render_template
from ...controller.auth import login


@page.route('/')
def index():
    return render_template('home/index.html', title="Welcome")
