from guts import app
from guts import db
from guts.models import User
from flask import session, redirect, url_for, render_template, flash

@app.route('/users/')
def list_users():
    users = User.query.all()
    return render_template("list_users.html", users=users)

@app.route('/users/add', methods=["POST"])
def add_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash("New User Added!")
    return redirect(url_for('list_users'))
