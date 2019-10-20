from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

application = Flask(__name__) # aws eb requires 'application' name for Flask instance

PG_URL = application.config.get('AWS_RDS_URL')
# should be pgmaster:postgres@doxa-database-staging.c8pjbrdeia2z.us-east-1.rds.amazonaws.com

application.config['SECRET_KEY'] = '7a273729d601733097ead8f655a410eb'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

if PG_URL is not None:
  application.config['SQLALCHEMY_DATABASE_URI'] = PG_URL
else:
  application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/doxa-db-dev'

db = SQLAlchemy(application)
from application import routes
from application import db

'''
dev setup commands:
Install PostgreSQL 11.5
(on MacOS use Homebrew -> brew install postgresql@11.5)
(not sure how on PC, but there is certainly an easy way)
start PostgreSQL -> brew services start postgresql
Then:
createdb doxa-db-dev
pip install
python manage.py db init
python manage.py db migrate (if you have new database changes)
Then inspect the new migration! Does it look okay?
python manage.py db upgrade (upgrades your database with new models)

you can query / inspect your database using:
psql doxa-db-dev

if the migration does not work, you can run 
python manage.py db downgrade
to undo it.

PR any new migrations
'''
