from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(1500),nullable=False)
    notes = db.relationship('Task', back_populates='owner', cascade='all, delete')