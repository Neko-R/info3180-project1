from flask import Flask
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Config Values
USERNAME = 'project1'
PASSWORD = 'project1'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

UPLOAD_FOLDER = './app/static/pro-pics'

app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://klpvgqzuvfyvlm:50d24867a9ecebafbdbf28f26b6940cc88b0f8b2eed7734006aa1e6e5a556447@ec2-54-197-232-203.compute-1.amazonaws.com:5432/dfkfpm70be1knh"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views