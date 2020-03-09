from flask import render_template, url_for, flash, redirect
from package import app,db 
from package.forms import RegistrationForm, LoginForm
from package.models import User
from flask_login import login_user
import pymongo
from pymongo import MongoClient

# Mongo Initialisation
cluster = MongoClient("mongodb+srv://admin:admin@cluster1-p71lz.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["Cluster1"]
collection = db["users"]

# Home Page
@app.route('/')
@app.route('/home')
def home():
    # online_users = mongo.db.users.find({"online": True})
    return render_template('home.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Login Model used to validate username exists in the Database
    # More than likely will not be used but more so for testing purposes
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            flash(f'Login Successful!', 'success')
            return redirect(url_for('loggedIn'))
        else:
             flash(f'Login Unsuccesful. Please make sure you have entered the correct details.', 'danger')
    return render_template('login.html', title='Login', form=form)

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # user = User(username=form.username.data, image=form.image.data)
        user_collection = cluster.db.collection
        user = {"username" : form.username.data, "image" : form.image.data}
        collection.insert_one(user)
        # db.session.add(user)
        # db.session.commit()
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/TestAdd')
def add_user():
    user_collection = cluster.db.collection
    user_collection.insert({'name' : 'Aaron'})
    user_collection.insert({'name' : 'Arnas'})
    user_collection.insert({'name' : 'Thomas'})
    return '<h1> Added a User!</h1>'

@app.route('/Camera')
def Camera():
    from python_files import faceLogin

@app.route('/loggedIn')
def loggedIn():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
    return render_template('loggedIn.html')