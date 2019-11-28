from application.app_setup import application
from application.initialize.db_init import db
from application.initialize.login_manager_init import login_manager
from application.initialize.bcrypt_init import bcrypt
from application.initialize.scheduler_jobstore_init import scheduler
from application.scheduled_data_tasks import job_scheduler
from application import routes

job_scheduler.schedule_jobs(scheduler)
