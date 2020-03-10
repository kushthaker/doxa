from application.initialize.scheduler_jobstore_init import scheduler
from application.models import User
import slack
import datetime as dt

NUDGE_KEYWORD = 'Fulfilled.ai-Nudge'

def schedule_nudge(nudge_type, **kwargs):
  nudge_function = NUDGES.get(nudge_type)
  job_name = f'{NUDGE_KEYWORD}-{nudge_type}-{kwargs}'
  if nudge_function:
    scheduler.add_job(nudge_function, kwargs=kwargs, name=job_name)
    print(f'Nudge scheduled: {job_name}')
    return True
  return False

def dnd_now(user_id=None, num_minutes=60):
  user = User.query.filter(User.id == user_id).one_or_none()
  if(not user): return False
  if(not user.fully_authenticated): return False
  slack_client = user.slack_user.slack_client()
  scheduled = slack_client.dnd_setSnooze(num_minutes=num_minutes).data
  print(scheduled)
  return scheduled

def dnd_after_hours(user_id=None, self_triggered=False):
  user = User.query.filter(User.id == user_id).one_or_none()
  if(not user): return False
  if(not user.fully_authenticated): return False
  now = dt.datetime.utcnow() + dt.timedelta(hours=12)
  current_time = now.time()
  
  # assumes user's workday end > workday start in hour of day (e.g. if you are in China / India, your UTC start time > UTC end time if you work morning to evening)
  user_start_time = user.workday_start.time()
  user_end_time = user.workday_end.time()
  if user_start_time < user_end_time:
    # non workday
    if (current_time < user_start_time) or (current_time > user_end_time):
      slack_client = user.slack_user.slack_client()
      schedule_end_time = dt.datetime(year=now.year, month=now.month, day=now.day, hour=user_start_time.hour, minute=user_start_time.minute)
      if now > schedule_end_time:
        schedule_end_time += dt.timedelta(days=1)
      time_diff = schedule_end_time - now - dt.timedelta(seconds=10)
      int_time_diff = int(time_diff.total_seconds()/60)
      scheduled = slack_client.dnd_setSnooze(num_minutes=int_time_diff).data
      print(scheduled)
      return scheduled
    # workday
    else:
      job_scheduler_time = dt.datetime(year=now.year, month=now.month, day=now.day, hour=user_end_time.hour, minute=user_end_time.minute) + dt.timedelta(minutes=1)
      if not self_triggered:
        kwargs = { 'user_id': user_id, 'self_triggered': True }
        scheduler.add_job(dnd_after_hours, next_run_time=job_scheduler_time, kwargs=kwargs, name=f"{NUDGE_KEYWORD}-{'dnd-after-hours'}-{kwargs}")
        print(f'scheduled dnd to be turned on later for user {user.username} at {job_scheduler_time}')
  
def open_calendar(user_id):
  user = User.query.filter(User.id == user_id).one_or_none()
  if(not user): return False
  if(not user.fully_authenticated): return False
  print(f'User {user.id} opened their calendar after a nudge.')

NUDGES = {
  'dnd-now': dnd_now,
  'dnd-after-hours': dnd_after_hours,
  'open-calendar': open_calendar
}
