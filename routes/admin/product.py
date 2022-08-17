#products routes routes/product.py



from flask import redirect,render_template,request,url_for
from run import app

@app.route('/add',methods=['GET','POST'])
def add():
    from models import Products,db
    if request.method=='POST':
        brand=request.form['u_brand']
        model=request.form['u_model']
        description=request.form['u_description']
        prdct=Products(brand=brand,model=model,description=description)
        db.session.add(prdct)
        db.session.commit()
        return redirect('/products')

    return render_template("admin/product/add.html")

@app.route('/products',methods=['GET','POST'])
def products():
    from models import Products,db
    products=Products.query.all()
    return render_template('admin/product/list.html',products=products)
    
    
@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    from models import Products,db
    prodct=Products.query.get(id)
    db.session.delete(prodct)
  
    db.session.commit()
    return redirect('/products')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    from models import Products,db
    product=Products.query.get(id)
    if request.method=='POST':

        product.brand=request.form['u_brand']
        product.model=request.form['u_model']
        product.description=request.form['u_description']
        db.session.commit()
        return redirect('/products')
    return render_template("admin/product/update.html",product=
    product)

