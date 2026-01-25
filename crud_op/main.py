from flask import Flask,render_template,request,redirect,url_for
from models import db,UserFeedback
from flask_login import LoginManager,Login_user,Login_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+mysqlconnector://root:root@localhost:3306/project2'
app.config["SECRET_KEY"] = "something"

db.init_app(app)
brcypt = Bcrypt(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user-id):
    return UserFeedback

with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        fname = request.form.get('name','')
        femail = request.form.get('email','')
        fmessage = request.form.get('message','')      
        user = UserFeedback(name=fname,email=femail,message=fmessage)  
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html')

@app.route('/feedback/')
def feedbacks():
    users = UserFeedback.query.all()
    return render_template('views_data.html',users = users)


@app.route('/feedback/<int:id>/') #url path convertor
def fb_message(id):
    user = UserFeedback.query.filter_by(id=id).first()
    return render_template('fb_message.html',user_data=user)


@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email = request.form.get('')
        password = request.form.get('')
        user = UserFeedback.query.filter_by(email=email).first()
        hash_pw = user.password
        if user:
            if bcrypt.check_password_hash(hash_pw,password):
                return redirect(url_for(dashbboard))
            else:
                return redirect(url_for('login'))
        else:
            return redirect(url_for('home'))
            
@app.route('/dashboard/')
def dashbboard():
    return render_template('dashboard.html')
            
