from flask import Blueprint, Response, render_template, flash, redirect, session, url_for, request, g
from app import app, db
from app.properties.forms import RegisterPropertyForm
from app.properties.models import Property


mod = Blueprint('properties', __name__)


@mod.route('/properties/', methods=('GET', 'POST'))
def property_view():
    form = RegisterPropertyForm(request.form)
    properties = Property.query.all()
    if form.validate_on_submit():
        property = Property()
        form.populate_obj(property)
        db.session.add(property)
        db.session.commit()
        return redirect('/properties/')
    return render_template('properties/index.html', form=form, properties=properties)
