from flask import Blueprint

misc_tools_blueprint = Blueprint('misc_tools_blueprint', __name__)

from . import misc_tools_routes  
