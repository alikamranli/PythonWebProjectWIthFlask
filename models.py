from run import db,app

class Messages(db.Model):
    id=db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    message = db.Column(db.String(200))

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name=db.column(db.String(20))
    surname = db.Column(db.String(20))
class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username=db.column(db.String(20))
    password=db.column(db.String(20))

class Backend(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    backend_admin_username=db.column(db.String(20))
    backend_admin_password=db.column(db.String(20))

class Frontend(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    frontend_admin_username=db.column(db.String(20))
    frontend_admin_password=db.column(db.String(20))