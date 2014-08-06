from mongoengine import *
from guts.models import *
from guts import app

julian = Coach(username="julian", email="julian")
julian.save()

