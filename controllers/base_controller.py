from flask import render_template, request, redirect
from flask import Blueprint

base_blueprint = Blueprint("base", __name__)


@base_blueprint.route('/')
def index():
    return render_template('index.html', title='Home')