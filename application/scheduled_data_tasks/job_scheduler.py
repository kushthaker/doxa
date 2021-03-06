from application.scheduled_data_tasks import apscheduler_util, slack_activities, \
            google_calendar_activities, github_activities, book_time, activity_summary

JOB_SCHEDULE = [
  {
    'func': slack_activities.capture_slack_activites_from_stored_raw_json,
    'trigger': apscheduler_util.build_minute_trigger(20)
  },
  {
    'func': slack_activities.capture_slack_conversation_reads,
    'trigger': apscheduler_util.build_minute_trigger(20)
  },
  {
    'func': slack_activities.capture_slack_conversations,
    'trigger': apscheduler_util.build_minute_trigger(5)
  },
  {
    'func': slack_activities.capture_slack_conversation_queries,
    'trigger': apscheduler_util.build_minute_trigger(5)
  },
  {
    'func': google_calendar_activities.update_google_calendar_events,
    'trigger': apscheduler_util.build_minute_trigger(15)
  },  
  {
    'func': book_time.book_upcoming_week_focus_time,
    'trigger': apscheduler_util.fridays_at_9AM_EST()
  },
  {
    'func': google_calendar_activities.refresh_google_credentials,
    'trigger': apscheduler_util.build_minute_trigger(30)
  },
  {
    'func': slack_activities.update_slack_users_data,
    'trigger': apscheduler_util.build_hour_trigger(2)
  },
  {
    'func': activity_summary.update_user_activity_rows_workday,
    'trigger': apscheduler_util.build_minute_trigger(15)
  },
  {
    'func': github_activities.capture_github_repos,
    'trigger': apscheduler_util.nightly_midnight_EST()
  },
  {
    'func': github_activities.capture_gitcommits_1hr,
    'trigger': apscheduler_util.build_hour_trigger(1)
  },
  {
    'func': github_activities.capture_gitcommits_30day,
    'trigger': apscheduler_util.nightly_midnight_EST()
  },
  {
    'func': github_activities.capture_gitissues_1hr,
    'trigger': apscheduler_util.build_hour_trigger(1)
  },
  {
    'func': github_activities.capture_gitissues_30day,
    'trigger': apscheduler_util.nightly_midnight_EST()
  },
  {
    'func': github_activities.capture_gitIssueComments_1hr,
    'trigger': apscheduler_util.build_hour_trigger(1)
  },
  {
    'func': github_activities.capture_gitIssueComments_30day,
    'trigger': apscheduler_util.nightly_midnight_EST()
  },
  {

    'func': activity_summary.update_user_activity_rows_non_workday,
    'trigger': apscheduler_util.build_hour_trigger(1)
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
