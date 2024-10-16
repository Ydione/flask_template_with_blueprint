from flask import Flask
from handlers import configure_routes

app = Flask(__name__, instance_relative_config=True, static_folder='static')

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
