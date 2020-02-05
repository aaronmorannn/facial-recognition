import os
from flask import Flask, render_template, url_for
app = Flask(__name__)


# Home Page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    return render_template('register.html')


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
