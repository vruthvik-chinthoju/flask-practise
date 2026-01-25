from flask import Flask,render_template
import mysql.connector

conn=mysql.connector.connect(
    user='root',
    password='root',
    host='localhost',
    port=3306,
    database='dummy_db'
)

cursor=conn.cursor()
app = Flask(__name__)

@app.route('/')
def home():
    cursor.execute('select * from dummy_table')
    data=cursor.fetchall()
    return render_template('home.html',datas=data)