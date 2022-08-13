#messages routes routes/message.py

from flask import redirect,render_template,request,url_for
from run import app

@app.route('/contact',methods=['GET','POST'])
def contact():
    from models import Messages,db
    if request.method=="POST":
        name=request.form['u_name']
        email=request.form['u_email']
        message=request.form['u_message']
        msj=Messages(name=name,email=email,message=message)
        db.session.add(msj)
        db.session.commit()
        return redirect('/messages')

    return render_template("contact.html")

@app.route('/messages',methods=['GET','POST'])
def messages():
    from models import Messages,db
    messages=Messages.query.all()
    return render_template('messages.html',messages=messages)
@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    from models import Messages,db
    mesaj=Messages.query.get(id)
    db.session.delete(mesaj)
  
    db.session.commit()
    return redirect('/messages')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    from models import Messages,db
    message=Messages.query.get(id)
    if request.method=='POST':
        
        message.name=request.form['u_name']
        message.email=request.form['u_email']
        message.message=request.form['u_message']
        db.session.commit()
        return redirect('/messages')
    return render_template("update.html",message=message)