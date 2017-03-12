from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Email, Length
from app.agents.models import Agent
from app.agencies.models import Agency
from app import db


def enabled_agencies():
    return Agency.query.all()


class RegisterAgentForm(FlaskForm):
    name = TextField(validators=[Required()])
    phone_number = TextField()
    email = TextField(validators=[Email()])
    agency = QuerySelectField(query_factory=enabled_agencies,
                              allow_blank=True)
