from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserFeedback(db.Model):
    id = db.Column(db.Integer,unique=True,primary_key=True,nullable=False,autoincrement=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False)
    message = db.Column(db.String(1500))
