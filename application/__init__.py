from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__) # aws eb requires 'application' name for Flask instance
application.config['SECRET_KEY'] = '7a273729d601733097ead8f655a410eb'

application.config['SLACK_CLIENT_ID'] = os.environ.get('SLACK_CLIENT_ID') # stored in EB config
application.config['SLACK_CLIENT_SECRET'] = os.environ.get('SLACK_CLIENT_SECRET') # stored in EB config

application.config['GITHUB_CLIENT_ID'] = os.environ.get('GITHUB_CLIENT_ID')
application.config['GITHUB_CLIENT_SECRET'] = os.environ.get('GITHUB_CLIENT_SECRET')

# For GitHub Enterprise
application.config['GITHUB_BASE_URL'] = 'https://HOSTNAME/api/v3/'
application.config['GITHUB_AUTH_URL'] = 'https://HOSTNAME/login/oauth/'

PG_URL = os.environ.get('AWS_RDS_URL')
if PG_URL != None:
  print('USING VARIABLE %s' % PG_URL)
  application.config['SQLALCHEMY_DATABASE_URI'] = PG_URL
  # to set AWS database URL for EB environment: `eb use _environment-name_` (e.g. doxa-staging) then `eb set-env _database-url_`
  # e.g. eb setenv AWS_RDS_URL=postgresql://pgmaster:postgres@database-url.rds.amazon.com:5432/doxa_db_staging
else:
  print('USING VARIABLE LOCAL')
  application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/doxa-db-dev'
 
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

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
pip install -r requirements.txt
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
