from flask import Flask,render_template

app = Flask(__name__,template_folder='htmlfolder')

@app.route('/')
def home():
   
    return render_template('home.html',student_data=student_data)

if __name__ == '__main__':
    app.run(port=67345,debug=True)