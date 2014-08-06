from flask import Flask
from mongoengine import connect
from flask.ext.foundation import Foundation

connect('guts-dev', host="mongodb://test:test@ds061199.mongolab.com:61199/guts-dev")

app = Flask(__name__)
Foundation(app)

app.config["SECRET_KEY"] = '\xc8\x83\xaf\xca,|\xdc\xbf\x87u`\x010w\xa4\xd5%\xb2\x1f\x19\x86\xc30\xee'

import guts.views
