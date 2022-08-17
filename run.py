from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project0.db'
db=SQLAlchemy(app)
migrate = Migrate(app, db)
from models import *
from routes.admin.product import *


db.create_all()
if __name__ == '__main__':
    app.run(port=5000,debug=True)