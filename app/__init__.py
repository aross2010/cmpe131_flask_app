
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

pathname = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # where the database file will be stored
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pathname, 'app.db')
)

db = SQLAlchemy(app)


from app import routes