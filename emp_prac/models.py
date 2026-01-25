from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False)
    department = db.Column(db.String(150),nullable=False)
    salary = db.Column(db.Integer,nullable=False)
