# /project/DM/views.py

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from forms import DM_Form
from project import db
from project.views import login_required
from project.models import DM


################
#### config ####
################

DM_blueprint = Blueprint(
    'DM', __name__,
    url_prefix='/DM',
    template_folder='templates',
    static_folder='static'
)


################
#### routes ####
################

@DM_blueprint.route('/DM/')
@login_required
def DM():
    Created_DM = db.session.query(DM)
    print Created_DM
    return render_template(
        'DM_table.html',
        Created_DM=Created_DM
    )


# Add new DM:
@DM_blueprint.route('/add/', methods=['GET', 'POST'])
@login_required
def new_DM():
    error = None
    form = DM_Form(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_DM = DM(
                form.DM_Vendor.data,
                form.DM_Product.data,
                form.DM_Email.data,
                form.DM_Description.data,
                session['user_id']
            )
            db.session.add(new_DM)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('DM.DM'))
        else:
            return render_template('DM_form.html', form=form, error=error)

# Delete DM:
@DM_blueprint.route('/delete/<DM_Product>/')
@login_required
def delete_entry(DM_Product):
    new_id = DM_Product
    DM = db.session.query(DM).filter_by(DM_Product=new_id)
    DM.delete()
    db.session.commit()
    flash('The Detection Mechanism was deleted')
    return redirect(url_for('DM_table.html'))
