# /project/Overview/views.py

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from project import db
from project.views import login_required


################
#### config ####
################

Overview_blueprint = Blueprint(
    'OverView', __name__,
    url_prefix='/Overview',
    template_folder='templates',
    static_folder='static'
)


################
#### routes ####
################

@Overview_blueprint.route('/Overview/')
@login_required
def Overview():
    return render_template(
                           'Overview.html',
                           username=session['name']
                           )
