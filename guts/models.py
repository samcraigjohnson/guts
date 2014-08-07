from mongoengine import Document, DateTimeField, StringField, ReferenceField, EmailField, ListField
import datetime

'''
Document is used to strictly adhere to the schema
DynamicDocument allows for any fields to be added and saved
All fields are optional enless required is set to True
'''

drill_list = []
LEVELS = ["Yellow", "Orange", "Purple"] 

class User(Document):
    username = StringField(max_length=50, required=True, unique=True)
    email = EmailField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    meta = {'allow_inheritance': True}

class Session(Document):
    time = DateTimeField(default=datetime.datetime.now)

class Coach(User):
    pass

class Player(User):
    level = StringField(max_length=10, choices=LEVELS)
    sessions = ListField(ReferenceField(Session))

#Super class for all drills
class Drill(Document):
    name = StringField(required=True)
    #TODO should deleting a player delete all of their drills?
    player = ReferenceField(Player)
    meta = {'allow_inheritance': True}
 
#Class specifically to do with elbow drill
class ElbowDrill(Drill):
    misses = StringField(required=True, max_length=10)

