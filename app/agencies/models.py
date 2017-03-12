from app import db
from app.mixins import CRUDMixin


class Agency(CRUDMixin, db.Model):
    __tablename__ = 'agencies'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text)
    address = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    email = db.Column(db.Text)

    # agents = db.relationship('Agent', back_populates='agency_id',
    #                          lazy='select')

    agents = db.relationship('Agent', back_populates='agency',
                             lazy='select')

    def __init__(self,
                 name=None,
                 address=None,
                 phone_number=None,
                 email=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return '%s' % (self.name)
