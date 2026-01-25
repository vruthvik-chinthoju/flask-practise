from flask import Flask,render_template

app=Flask(__name__,template_folder='htmlfolder',static_folder='stylingfolder')


@app.route('/')
def  home():
    return render_template('home.html')


@app.route('/contact/')
def contactme():
    return render_template('contact.html')

@app.route('/about/')
def aboutme():
    return render_template('about.html')

