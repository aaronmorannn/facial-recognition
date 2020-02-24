from flask import Flask, render_template, url_for
from application import app
from application.forms import RegistrationForm, LoginForm
from application.models import User


# Home Page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Login Page
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

# Register Page
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)


@app.route('/test')
def TEST():
    return "Testing..."