from guts import db
from flask.ext.security import UserMixin, RoleMixin
import datetime

'''
Document is used to strictly adhere to the schema
DynamicDocument allows for any fields to be added and saved
All fields are optional enless required is set to True
'''

drill_list = []

LEVELS = ["Yellow", "Orange", "Purple"] 

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    username = db.StringField(max_length=50)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    email = db.StringField(max_length=255)
    confirmed_at = db.DateTimeField()

    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    roles = db.ListField(db.ReferenceField(Role), default=[])

    meta = {'allow_inheritance': True}
    
class Session(db.Document):
    time = db.DateTimeField(default=datetime.datetime.now)

class Coach(User):
    pass

class Player(User):
    level = db.StringField(max_length=10, choices=LEVELS)
    sessions = db.ListField(db.ReferenceField(Session))

#Super class for all drills
class Drill(db.Document):
    name = db.StringField(required=True)
    #TODO should deleting a player delete all of their drills?
    player = db.ReferenceField(Player)
    meta = {'allow_inheritance': True}
 
#Class specifically to do with elbow drill
class ElbowDrill(Drill):
    misses = db.StringField(required=True, max_length=10)
