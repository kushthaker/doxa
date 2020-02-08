from flask_bcrypt import Bcrypt
from application.app_setup import application

bcrypt = Bcrypt(application)
