# project/__init__.py


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.migrate import Migrate

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.users.views import users_blueprint
from project.DM.views import DM_blueprint
from project.Overview.views import Overview_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(DM_blueprint)
app.register_blueprint(Overview_blueprint)
