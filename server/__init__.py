import os

import logging
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DevelopmentConfig

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "hello world!"


app_settings = DevelopmentConfig
app.config.from_object(app_settings)
app.logger.setLevel(logging.DEBUG)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from views import vendor_bp
app.register_blueprint(vendor_bp)
