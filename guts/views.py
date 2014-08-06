from guts import app
from guts.models import *
from guts.forms import *
from flask import session, redirect, url_for, render_template, flash

@app.route('/')
def index():
    return render_template("list_users.html", users=User.objects, title="Users")

@app.route('/players/')
def list_users():
    return render_template("list_users.html", users=Player.objects, title="Players")

@app.route('/coach/admin', methods=["POST", "GET"])
def add_player():
    form = AddPlayerForm()
    if form.validate_on_submit():
        return "SUCESS!!"
    return render_template("admin.html", add_player_form=form)
