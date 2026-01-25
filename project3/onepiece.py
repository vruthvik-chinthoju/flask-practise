from flask import Flask,render_template
import mysql.connector

app = Flask(__name__,template_folder="htmlfolder")

conn=mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    port=3306,
    database='office'
)
cursor=conn.cursor()
app = Flask(__name__)


@app.route('/')
def anime():
    cursor.execute('select * from employee')
    data=cursor.fetchall()
    print(data)
    return render_template('new.html',employee=data)

