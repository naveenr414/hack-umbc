from flask_wtf import Form
from wtforms import StringField, SubmitField

class AddressForm(Form):
    address = StringField("Address")
    submit = SubmitField('Sign In')
