# views , routes code

from flask import redirect, render_template, url_for
from main_app import app, db
from flask_sqlalchemy import SQLAlchemy
from flask import request


@app.route("/")
def routePage():

    return render_template("/adminpanel/index.html")


@app.route('/login/')
def login():   
    return render_template('login.html')
    
@app.route('/submit/', methods=['POST'])
def submitForm():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        return render_template('/adminpanel/index.html', username = username, password = password, email=email)
    except Exception as ex:
        return ex   



@app.route('/home/')
def homePage():
    name = "Tarokh"
    age = 17
    users = db.users.query.all()
    return render_template('index.html', users=users)

@app.route('/about/')
def aboutPage():
    
    return render_template('about.html')
