
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
import quiz_app.db_config as conf
import os

app = Flask(__name__)
db_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/pythonquestions.db'))
app.secret_key = "pythonquestions-database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s"%db_file
db = SQLAlchemy(app)

from quiz_app import routes