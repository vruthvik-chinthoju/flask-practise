from flask import Flask,render_template,request
# from models import db

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]='mysql+mysqlconnector://root:root@localhost:3306/project2'
# db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/',methods=['GET','POST'])
def contact():
    if request.method =='POST':
        name = request.form.get('user_name',None)
        email = request.form.get('user_email',None)
        message = request.form.get('user_message',None)
        return render_template('data_rep.html',data_name=name,data_email=email,data_message=message)
    return render_template('contact.html')
