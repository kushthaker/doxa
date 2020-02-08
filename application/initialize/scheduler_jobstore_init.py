from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from application.initialize.config import Config
from application.app_setup import application

jobstore = SQLAlchemyJobStore(url=Config.SQLALCHEMY_DATABASE_URI)
application.config['SCHEDULER_JOBSTORES'] = {
  'default': jobstore
}
application.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

scheduler = BackgroundScheduler()
scheduler.add_jobstore(application.config.get('SCHEDULER_JOBSTORES').get('default'))
print('starting scheduler...')
scheduler.start()
