from application.app_setup import application
from flask_cors import CORS
from application.initialize.config import Config
application.config['CORS_HEADERS'] = Config.CORS_HEADERS
cors = CORS(application, resources={r"/*": {"origin": "*"}})
