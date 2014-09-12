# project/models.py


from project import db


class DM(db.Model):

    __tablename__ = "DM"

    DM_Vendor = db.Column(db.String, nullable=True)
    DM_Product = db.Column(db.String, primary_key=True)
    DM_Email = db.Column(db.String, unique=True, nullable=False)
    DM_Description = db.Column(db.String, nullable=True)


    def __init__(self, DM_Vendor, DM_Product, DM_Email, DM_Description):

        self.DM_Vendor = DM_Vendor
        self.DM_Product = DM_Product
        self.DM_Email = DM_Email
        self.DM_Description = DM_Description

    def __repr__(self):
        return '<name %r>' % (self.name)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, default='user')

    def __init__(self, name=None, email=None, password=None, role=None):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % (self.name)
