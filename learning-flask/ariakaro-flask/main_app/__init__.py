import mysql.connector
from flask import Flask
from flask import render_template
from mysql.connector import Connect, Error


app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="management"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
    ...

import main_app.views
import main_app.models


if __name__ == '__main__':
    
    app.run(host='localhost', debug=True)