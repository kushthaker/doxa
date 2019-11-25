from application.models import SlackUser, RawSlackEvent, SlackUserEvent
from application import db
from datetime import datetime

def capture_slack_activites_from_stored_raw_json():
  raw_slack_events = RawSlackEvent.query.all()
  raw_slack_event_count = len(raw_slack_events)
  total_new_slack_events = 0
  for event in raw_slack_events:
    raw_event_json = event.json_data
    if (raw_event_json.get('event')) \
    and (raw_event_json.get('event').get('user')) \
    and type((raw_event_json.get('event').get('user'))) == str:
      # getting data around user, checking to see if event has not already been created
      slack_user_api_id = raw_event_json.get('event').get('user')
      slack_event_api_id = raw_event_json.get('event_id')
      slack_user = SlackUser.query.filter_by(slack_user_api_id=slack_user_api_id).one_or_none()
      slack_event = SlackUserEvent.query.filter_by(slack_event_api_id=slack_event_api_id).one_or_none()
      if slack_user and (not slack_event):
        # creating object, adding to DB session. (then all objects get saved at once, at the bottom)
        slack_user_id = slack_user.id
        raw_slack_event_id = event.id
        slack_event_type = raw_event_json.get('event').get('type')
        slack_event_subtype = raw_event_json.get('event').get('subtype')
        event_datetime = datetime.fromtimestamp(raw_event_json.get('event_time'))
        last_updated = datetime.utcnow()
        new_slack_event = SlackUserEvent( \
          slack_user_id=slack_user_id,
          slack_event_api_id=slack_event_api_id,
          raw_slack_event_id=raw_slack_event_id,
          slack_event_type=slack_event_type,
          event_datetime=event_datetime,
          last_updated=last_updated
        )
        db.session.add(new_slack_event)
        total_new_slack_events += 1
  db.session.commit()
  print('Created %s new SlackUserEvents in DB out of %s total raw Slack events' % (total_new_slack_events, raw_slack_event_count))
