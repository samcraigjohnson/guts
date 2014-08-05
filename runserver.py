from guts import app
from guts import db
from guts.models import User
'''
db.create_all()
sam = User('sam', 'sam@sam.com')
db.session.add(sam)
db.session.commit()'''

app.run(debug=True)
