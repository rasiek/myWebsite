from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
    print("this works")
    print(os.environ.get('DATABASE_URI'))
else:
    app.config.from_object("config.DevelopmentConfig")


db = SQLAlchemy(app)
print(db)

print(f'ENV is set to: {app.config["ENV"]}')



from app import views, admin_views, contact_views, models
