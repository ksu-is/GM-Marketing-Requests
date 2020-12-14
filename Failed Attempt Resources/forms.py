from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField

class RequestForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    location = StringField('Property')
    date = StringField('Date Needed')
    submit = SubmitField('Submit')