from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


db = SQLAlchemy(app)

print(f'ENV is set to: {app.config["ENV"]}')



from app import views, admin_views, contact_views, models
