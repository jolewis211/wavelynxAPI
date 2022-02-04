from flask_api import FlaskAPI, status
import dummyapi.token as token
from flask_sqlalchemy import SQLAlchemy
import os

app = FlaskAPI(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'\
     + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)