import sqlalchemy
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/management"
#app.config['SECRET_KEY'] = "SPM5axwkh|nl@L2PcQm$uUgwBtu#JKIfH1f"
db = SQLAlchemy(app)
engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/management", convert_unicode=True)
conn = engine.connect()
res = db.select()

Base = declarative_base()
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = db_session()


import main_app.views
import main_app.models


if __name__ == '__main__':
    
    app.run(host='localhost', debug=True)