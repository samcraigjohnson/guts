from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AddPlayerForm(Form):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

