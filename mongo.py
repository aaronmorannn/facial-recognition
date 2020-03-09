from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'users_database'
app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster1-p71lz.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


if __name__ == '__main__':
    app.run(debug=True)