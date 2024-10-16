"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from flask_bootstrap import Bootstrap5
import os
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from .assets import compile_stylesheet_bundles, compile_js_bundles

# Create all databases here
db = SQLAlchemy()

def configure_routes(app):
    """Create Flask application."""
    app.config.from_object("handlers.config.Config")
    Bootstrap5(app)
    assets = Environment()
    assets.init_app(app)

    moment = Moment(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') # main db
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from home import home_blueprint
        from misc_tools import misc_tools_blueprint

        # Register Blueprints
        app.register_blueprint(home_blueprint)      
        app.register_blueprint(misc_tools_blueprint)      

        # db.create_all()      

        # Compile static assets
        compile_stylesheet_bundles(assets)
        compile_js_bundles(assets)

        return app
    if __name__ == "__main__":
        app.run(ssl_context="adhoc")
