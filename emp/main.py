from flask import Flask,render_template,request,redirect,url_for
from models import db,Employee

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+mysqlconnector://root:root@localhost:3306/project2'
app.config["SECRET_KEY"] = "something"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def home():
    if request.method =='POST':
        emp_name = request.form.get('name','')
        emp_email = request.form.get('email','')
        dept_no = request.form.get('dept_no','')
        emp_salary = request.form.get('salary','')
        user = Employee(name=emp_name,email=emp_email,dept_no=dept_no,salary=emp_salary)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    emps = Employee.query.all()
#     return render_template('home.html',emps=emps)


# @app.route('/all/<int:id>')
# def entire_data(id):
#     employees = Employee.query.filter_by(id=id).first()
#     return render_template('emp_all.html',emp=employees)
    emp_id = request.args.get('id')
    choose_emp = None

    if emp_id:
        choose_emp = Employee.query.get(emp_id)


    return render_template('home.html',emps=emps,selected=choose_emp)



