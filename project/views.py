# project/views.py


#################
#### imports ####
#################

from project import app, db
from project.models import DM
from flask import flash, redirect, session, url_for, \
    render_template, request, jsonify, make_response
from functools import wraps
import datetime


##########################
#### helper functions ####
##########################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error), 'error')


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


################
#### routes ####
################

@app.route('/', defaults={'page': 'index'})
def index(page):
    return(redirect(url_for('users.login')))


########################
#### error handlers ####
########################

@app.errorhandler(404)
def page_not_found(error):
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write("\n404 error at {}: {} ".format(current_timestamp, r))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    if app.debug is not True:
        now = datetime.datetime.now()
        r = request.url
        with open('error.log', 'a') as f:
            current_timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write("\n500 error at {}: {} ".format(current_timestamp, r))
    return render_template('500.html'), 500


#######################
#### API Endpoints ####
#######################

@app.route('/api/DM/', methods=['GET'])
def DMs():
    if request.method == 'GET':
        results = db.session.query(DM).offset(0).all()
        json_results = []
        for result in results:
            data = {
                'DM_Vendor': result.DM_Vendor,
                'DM_Product': result.DM_Product,
                'DM_Email': result.DM_Email,
                'DM_Description': result.DM_Description
            }
            json_results.append(data)

    return jsonify(items=json_results)


@app.route('/api/DM/<DM_Product>')
def DM(DM_Product):
    if request.method == 'GET':
        result = db.session.query(DM).filter_by(DM_Product=DM_Product).first()
        if result:
            result = {
                'DM_Vendor': result.DM_Vendor,
                'DM_Product': result.DM_Product,
                'DM_Email': result.DM_Email,
                'DM_Description': result.DM_Description
            }
            code = 200
        else:
            result = {"sorry": "Element does not exist"}
            code = 404
        return make_response(jsonify(result), code)
