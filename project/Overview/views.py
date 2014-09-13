# /project/Overview/views.py

from flask import render_template, session, Blueprint
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
    return render_template('Overview.html', username=session['name'])
