from qanda import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable = False)
    lname = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(11), unique = True, nullable = False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    password = db.Column(db.String(300), nullable=False)
    account_details = db.relationship('AccountDetails', backref='user', lazy=True)

    def __str__(self):
        return f"User {self.username}"

class AccountDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(80), nullable = False)
    account_number = db.Column(db.String(10), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)

    def __str__(self):
        return self.bank_name