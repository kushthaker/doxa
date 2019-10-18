from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__) # aws eb requires 'application' name for Flask instance

application.config['SECRET_KEY'] = '7a273729d601733097ead8f655a410eb'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(application)

from application import routes
