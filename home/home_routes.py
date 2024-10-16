# This file contains all routes under 'home' blueprint
from flask import render_template
from . import home_blueprint

@home_blueprint.route("/", methods=["GET"])
def home_dashboard():
    return render_template('home/home.html')