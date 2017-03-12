from flask import Blueprint, Response, render_template, flash, redirect, session, url_for, request, g
from app import app, db
from app.agents.forms import RegisterAgentForm
from app.agents.models import Agent


mod = Blueprint('agents', __name__)


@mod.route('/agents/', methods=('GET', 'POST'))
def agents_view():
    form = RegisterAgentForm(request.form)
    agents = Agent.query.all()
    if form.validate_on_submit():
        agent = Agent()
        form.populate_obj(agent)
        db.session.add(agent)
        db.session.commit()
        return redirect('/agents/')
    return render_template('agents/index.html', form=form, agents=agents)
