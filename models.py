from run import db,app

class Messages(db.Model):
    id=db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    message = db.Column(db.String(200))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(100))
    password=db.Column(db.String(100))
    is_logged_in=db.Column(db.Boolean)

