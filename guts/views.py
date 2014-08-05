from guts import app
from guts import db
from guts.models import User

@app.route('/')
def index():
    users = User.query.all()
    print users
    return "hello " + users[0].username
