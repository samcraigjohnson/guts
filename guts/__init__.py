from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore

#set up app
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xc8\x83\xaf\xca,|\xdc\xbf\x87u`\x010w\xa4\xd5%\xb2\x1f\x19\x86\xc30\xee'

#set up configuration for flask-security
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = '5f4ad6a5e2054c74b72a50f09a94f0e3'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

#mongo config
app.config['MONGODB_DB'] = 'guts-dev'
app.config['MONGODB_HOST'] = 'mongodb://test:test@ds061199.mongolab.com:61199/guts-dev'
app.config['MONGODB_PORT'] = 61199

#create db connection
db = MongoEngine(app)

#setup security
from guts.models import Role, User
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#required by flask import of views
import guts.views
