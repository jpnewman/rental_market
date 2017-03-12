from app import db
from app.mixins import CRUDMixin


class Agent(CRUDMixin, db.Model):
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    email = db.Column(db.Text)

    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'))
    agency = db.relationship('Agency', back_populates='agents')

    def __init__(self,
                 name=None,
                 phone_number=None,
                 email=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return '<Agent %r>' % (self.name)
