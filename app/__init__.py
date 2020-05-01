from flask import Flask
from config import DevelopementConfig
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(DevelopementConfig)
db = SQLAlchemy(app)



from app import views, admin_views, contact_views, models
