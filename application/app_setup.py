from application.initialize.config import Config
from flask import Flask

'''
aws eb requires 'application' name for Flask instance
This file needs to be in the `application` folder because
the `__name__` variable is referenced by jinja2 for templating
'''

application = Flask(__name__)
application.config['SECRET_KEY'] = Config.APPLICATION_SECRET_KEY
