import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

# PyMongo Initialisation
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)

# Setting up CSRF Protection which was interfering with the Server
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# INTERNAL SERVER ISSUE FIX
csrf = CSRFProtect(app)
# configuring database using SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)

from package import routes