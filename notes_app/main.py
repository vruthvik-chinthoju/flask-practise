from flask import Flask,render_template,redirect,request,flash,url_for
from models import User,db
from flask_login import LoginManager,login_user,login_required
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycorg2://postgres:root@locahost:5432/notes_app'
app.secret_key = 'secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        email_exists = User.query.filter_by(email=email).first()
        if email_exists:
            flash("Email Already Exists")
            return redirect(url_for('login'))
        else:
            password = request.form.get('password')
            hashed_password = generate_password_hash(password)
            user = User(name=name,email=email,password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash("Account Registered")
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login/',methods=['GET,POST'])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect Password")
                return redirect(url_for('login'))
        else:
            flash("Email Not Found")
            return redirect(url_for('signup')) 
    return render_template('login.html')
       


