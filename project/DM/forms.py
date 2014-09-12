# /project/DM/forms.py


from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class DM_Form(Form):
    DM_Vendor = TextField('DM_Vendor')
    DM_Product = TextField('DM_Product', DataRequired())
    DM_Email = TextField(
        'DM_Email',
        validators=[Email(), Length(min=6, max=50)]
    )
    DM_Description = TextAreaField('DM_Description')
