from run import db,app

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    brand=db.Column(db.String(100))
    model=db.Column(db.String(100))
    description=db.Column(db.String(200))
    

class Orders(db.Model):
    id=db.Column(db. Integer,primary_key=True,autoincrement=True)
    order_date=db.Column(db.DateTime)
    order_status=db.Column(db.String(100))
    order_total=db.Column(db.Integer, )
    is_active=db.Column(db.Boolean, default=True)
    add_date=db.Column(db.DateTime)