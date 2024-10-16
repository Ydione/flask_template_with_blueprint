"""Class-based Flask app configuration."""
import subprocess
from os import environ, path

from dotenv import load_dotenv



BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Configuration from environment variables."""

    # General Config\
    VAR_1 = environ.get('VAR_1')

    # Flask Config
    SECRET_KEY = environ.get('APP_SECRET_KEY')
    FLASK_DEBUG = environ.get("FLASK_DEBUG")

    # Static Assets
    STATIC_FOLDER = "assets"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = False

    # Configuration

    # App Defaults
    N_DAYS = 7
    SPECIAL_CASE = ""
    DISCLAIMER = ""
    COLORS = ["#f7db4f","#2f9599","#a6236e","#EE7214","#5F6F52","B99470","#A9B388","#EE7214","#9e9e9e","#ec2049"]

    # Flask-Assets
    # if ENVIRONMENT == "development":
    #     # Check if `lessc` is installed
    #     LESS_BIN = subprocess.call("which lessc", shell=True)
    #     if LESS_BIN is None:
    #         raise ValueError("Flask requires `lessc` to be installed to compile styles.")
    #     else:
    #         # Check if `nodejs` is installed
    #         NODE_JS = subprocess.call("which node", shell=True)
    #         if NODE_JS is None:
    #             raise ValueError(
    #                 "Application running in `development` mode cannot create assets without `node` installed."
    #             )

    # Hardcoded data

    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True