from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required, Email, Length
from app.properties.models import Property
from app import db


class RegisterPropertyForm(FlaskForm):
    name = TextField(validators=[Required()])
    address = TextField()
