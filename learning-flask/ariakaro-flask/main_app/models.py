from main_app import db
from datetime import datetime

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f"{self.username}, {self.email}, {self.password}"
    

    
#db.create_all()