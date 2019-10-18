from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__) # aws eb requires 'application' name for Flask instance
app = application

app.config['SECRET_KEY'] = '7a273729d601733097ead8f655a410eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from application import routes
