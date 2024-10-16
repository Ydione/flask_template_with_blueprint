from flask import send_file

# This file contains all routes under 'misc_tools' blueprint
from flask import render_template
from . import misc_tools_blueprint

@misc_tools_blueprint.get("/misc_tools")
def misc_tools_dashboard():
    return "misc_tools"

@misc_tools_blueprint.get("/favicon.ico")
def get_favicon():
    filename = 'static/img/favicon.ico'
    return send_file(filename, mimetype='image/ico')