from flask_login import LoginManager
from application.app_setup import application

login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'