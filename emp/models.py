from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer,unique=True,autoincrement=True,primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False)
    dept_no = db.Column(db.Integer,nullable=False)
    salary = db.Column(db.Integer,nullable=False)