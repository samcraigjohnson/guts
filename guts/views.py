from guts import app
from guts.models import *
from flask import session, redirect, url_for, render_template, flash

@app.route('/')
def index():
    return render_template("list_users.html", users=User.objects, title="Users")

@app.route('/players/')
def list_users():
    return render_template("list_users.html", users=Player.objects, title="Players")

@app.route('/users/add', methods=["POST"])
def add_user():
    #user = User(request.form['username'], request.form['email'])
    #db.session.add(user)
    #db.session.commit()
    #flash("New User Added!")
    return redirect(url_for('list_users'))
