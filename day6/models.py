from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from views import app

class Base(DeclarativeBase):
  pass

db = SQLAlchemy()

class UserMessage(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False,unique=True)
    message = db.Column(db.String(150),nullable=False)


