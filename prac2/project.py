from flask import Flask,render_template

obj = Flask(__name__)


# @obj.route('/')
# def home():
#     return render_template('home.html')


@obj.route('/')
def details():
    return render_template('details.html',name='LUFFY',role='ADVENTURE',dept='python',friend='',number=[1,2,3,4,5])