from flask import render_template, url_for, flash, redirect
from package import app, db 
from package.forms import RegistrationForm, LoginForm
from package.models import User
from flask_login import login_user

# Home Page
@app.route('/')
@app.route('/home')
def home():
    # online_users = mongo.db.users.find({"online": True})
    return render_template('home.html')

# Login Page
@app.route('/login')
def login():
    form = LoginForm()
    # Login Model used to validate username exists in the Database
    # More than likely will not be used but more so for testing purposes
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            flash(f'Login Succesful.!', 'success')
            return redirect(url_for('home'))
        else:
             flash(f'Login Unsuccesful.!', 'danger')
    return render_template('login.html', title='Login', form=form)

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/test')
def TEST():
    return "Testing..."