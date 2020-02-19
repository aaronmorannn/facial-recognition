from __main__ import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # MAX 20 chars
    username = db.Column(db.String(20), unique=True, nullable=False)
    # Add default image to code
    image = db.Column(db.String(20), nullable=False, default='scan.jpg')

    def __repr__(self):
        return f"User('{self.username}', '{self.image}')"
