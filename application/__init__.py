import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)


# configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from face-recog import routes