from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.triggers.cron import CronTrigger
from time import gmtime, strftime
from application.models import SlackUser

def add_or_update_job_from_function(scheduler, **kwargs):
  func = kwargs.get('func')
  assert func
  if not kwargs.get('name'):
    name = func.__name__
    kwargs['name'] = name
  listed_jobs = scheduler.get_jobs()
  job_exists = False
  existing_job = None
  job_ids = [0]
  for job in listed_jobs:
    if job.func == func:
      job_exists = True
      existing_job = job
    job_ids.append(int(job.id))

  if job_exists:
    job = scheduler.modify_job(job_id=existing_job.id, **kwargs)
    if job.trigger:
      job = scheduler.reschedule_job(job_id=job.id, trigger=job.trigger)
    return job
  else:
    max_job_id = str(max(job_ids) + 1)
    kwargs['id'] = max_job_id
    return scheduler.add_job(**kwargs)

def test_running_task():
  time_string = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  print("Scheduled task run successfully at %s" % time_string)

def test_sum_two_numbers(one=1, two=2):
  print("sum: % s" % (one + two))

def create_three_test_tasks(scheduler):
  print(add_or_update_job_from_function(scheduler, func=test_running_task, trigger=build_minute_trigger(5)))
  print(add_or_update_job_from_function(scheduler, \
                                        func=test_sum_two_numbers, trigger=build_minute_trigger(15), args=(2, 3)))

def build_second_trigger(seconds):
  trigger = CronTrigger(second='*/%s' % seconds)
  return trigger

def build_minute_trigger(minutes):
  trigger = CronTrigger(minute='*/%s' % minutes)
  return trigger

def build_hour_trigger(hours):
  trigger = CronTrigger(hour='*/%s' % hours)
  return trigger
