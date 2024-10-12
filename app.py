"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
from flask_bootstrap import Bootstrap5
import os
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from assets import compile_stylesheet_bundles, compile_js_bundles

# Create all databases here
db = SQLAlchemy()

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=True, static_folder='static')
    app.config.from_object("config.Config")
    Bootstrap5(app)
    assets = Environment()
    assets.init_app(app)

    moment = Moment(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') # main db
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from home import home_blueprint

        # Register Blueprints
        app.register_blueprint(home_blueprint)      

        # db.create_all()      

        # Compile static assets
        compile_stylesheet_bundles(assets)
        compile_js_bundles(assets)

        return app
    if __name__ == "__main__":
        app.run(ssl_context="adhoc")
