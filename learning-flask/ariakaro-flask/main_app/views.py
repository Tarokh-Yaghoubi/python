# views , routes code

from flask import redirect, render_template, url_for
from main_app import app, mysql
from flask import request


# creating a cursor : 

with app.app_context():
    cursor = mysql.connection.cursor()

# Routing : 


@app.route("/")
def routePage():

    return render_template("/adminpanel/index.html")


@app.route('/login/')
def login():   
    return render_template('login.html')
    

@app.route('/submit/', methods=['GET', 'POST'])
def submitForm():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['firstname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        connection = mysql.connection.get_connection()
        cursor = connection.cursor()
        adduser_query = ''' INSERT INTO users (name, email, username, password) VALUES(%s,%s,%s,%s)''',(name,email,username,password)
        cursor.execute(adduser_query)
        connection.commit()
        cursor.close()
        return render_template("/adminpanel/index.html")
    
    return "ok"   


@app.route("/users/")
def usersInfo():
    select_user_query = 'SELECT * FROM users'
    cursor.execute(select_user_query)
    data = cursor.fetchall()
    
    return render_template('users.html', value=data)



@app.route('/home/')
def homePage():
    name = "Tarokh"
    age = 17
    return render_template('index.html')

@app.route('/about/')
def aboutPage():
    
    return render_template('about.html')


