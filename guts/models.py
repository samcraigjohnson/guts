from mongoengine import Document, StringField, ReferenceField

class User(Document):
    username = StringField(max_length=50)
    email = StringField(required=True)

    meta = {'allow_inheritance': True}

class Coach(User):
    pass

class Player(User):
    level = StringField(max_length=10)

#Super class for all drills
class Drill(Document):
    name = StringField(required=True)
    #TODO should deleting a player delete all of their drills?
    player = ReferenceField(Player)
    meta = {'allow_inheritance': True}
 
#Class specifically to do with elbow drill
class ElbowDrill(Drill):
    misses = StringField(required=True, max_length=10)
