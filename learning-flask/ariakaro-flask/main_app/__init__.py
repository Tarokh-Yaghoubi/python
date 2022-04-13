from flask import Flask, render_template
import mysql.connector
from flask_mysqlpool import MySQLPool


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'management'
app.config['MYSQL_POOL_NAME'] = 'mysql_pool'
app.config['MYSQL_POOL_SIZE'] = 30
app.config['MYSQL_AUTOCOMMIT'] = True



mysql = MySQLPool(app)

import main_app.views


if __name__ == '__main__':
    
    app.run(host='localhost', debug=True)