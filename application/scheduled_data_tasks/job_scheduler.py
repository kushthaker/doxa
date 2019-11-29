from application.scheduled_data_tasks import apscheduler_util, slack_activities

JOB_SCHEDULE = [
  {
    'func': slack_activities.capture_slack_activites_from_stored_raw_json,
    'trigger': apscheduler_util.build_hour_trigger(1)
  },
  {
    'func': slack_activities.capture_slack_conversations,
    'trigger': apscheduler_util.build_hour_trigger(1)
  },
  {
    'func': slack_activities.capture_slack_conversation_queries,
    'trigger': apscheduler_util.build_minute_trigger(5)
  }
]

def schedule_jobs(scheduler):
  func_list = [job['func'] for job in JOB_SCHEDULE]
  current_jobs = scheduler.get_jobs()
  for job in current_jobs:
    if job.func not in func_list:
      scheduler.remove_job(job.id)
  for job_details in JOB_SCHEDULE:
    apscheduler_util.add_or_update_job_from_function(scheduler, **job_details)

  print('Jobs scheduled:')
  print(scheduler.get_jobs())
