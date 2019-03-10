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
app.config['SQLALCHEMY_DATABASE_URI'] = "'postgresql://lpgaueufxtupxk:c827a24e8428cdc85ab6d2f18d487cee9e7a85b36eec095bd467b589016e79d3@ec2-54-221-236-144.compute-1.amazonaws.com:5432/ddvirpdt68llo5'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views