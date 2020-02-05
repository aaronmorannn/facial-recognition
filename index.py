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

# Localhost setup - http://localhost:5000/
if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='localhost', port=port)
