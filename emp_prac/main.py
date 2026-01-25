from flask import Flask,render_template,request,redirect,url_for
from models import db,Employee

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+mysqlconnector://root:root@localhost:3306/project1'
app.config["SECRET_KEY"]= "something"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/',methods=['POST','GET'])
def emp():
    if request.method =='POST':
        emp_name = request.form.get('name','')
        emp_email = request.form.get('email','')
        emp_department = request.form.get('department','')
        emp_salary = request.form.get('salary','')
        user = Employee(name=emp_name,email=emp_email,department=emp_department,salary=emp_salary)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('emp'))
    employees = Employee.query.all()
    
    emp_id = request.args.get("id")
    selected = None
    if emp_id :
        selected = Employee.query.get(int(emp_id))

    return render_template('home.html',emps=employees,selected=selected)

@app.route('/update/<int:id>/',methods=['GET','POST'])
def update(id):
    emp = Employee.query.get(id)
    if request.method=='POST':
        emp.name = request.form['name']
        emp.email = request.form['email']
        emp.department = request.form['department']
        emp.salary = request.form['salary']
        db.session.commit()
        return redirect(url_for('emp'))

    return redirect(url_for('emp'))


@app.route('/delete/<int:id>/')
def delete(id):
    emp = Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for('emp'))


