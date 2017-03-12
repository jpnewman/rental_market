from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required, Email, Length
from app.agencies.models import Agency
from app import db


class RegisterAgencyForm(FlaskForm):
    name = TextField(validators=[Required()])
    address = TextField()
    phone_number = TextField()
    email = TextField(validators=[Email()])
