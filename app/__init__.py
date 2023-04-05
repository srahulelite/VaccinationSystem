from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = '571ebfo2784rjsd'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///doctor_patient_info.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
app.app_context().push()

app.config.from_object('config')

from app import views
from app import models