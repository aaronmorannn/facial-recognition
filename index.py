import os
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f8f554e6ee2289a018a19ae92f1c6325'

# import secrets
# secrets.token_hex(16)
# 'f8f554e6ee2289a018a19ae92f1c6325'


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


# Localhost setup - http://localhost:5000/
if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='localhost', port=port)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
