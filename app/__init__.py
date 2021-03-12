from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


db = SQLAlchemy(app)



from app import views, contact_views, models
