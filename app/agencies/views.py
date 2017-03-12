from flask import Blueprint, Response, render_template, flash, redirect, session, url_for, request, g
from app import app, db
from app.agencies.forms import RegisterAgencyForm
from app.agencies.models import Agency
from flask import make_response, jsonify


mod = Blueprint('agencies', __name__)


@mod.route('/agencies/', methods=('GET', 'POST'))
def agencies_view():
    form = RegisterAgencyForm(request.form)
    agencies = Agency.query.all()
    if form.validate_on_submit():
        agency = Agency()
        form.populate_obj(agency)
        db.session.add(agency)
        db.session.commit()
        return redirect('/agencies/')
    return render_template('agencies/index.html', form=form, agencies=agencies)

@mod.route('/agencies/<int:id>', methods=['DELETE'])
def delete_entry(id):
     agency = Agency.query.get(id)

     if agency:
         agency.delete(True)

     return make_response(jsonify(agency=agency), 201)
