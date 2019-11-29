from application.models import SlackUser, RawSlackEvent, \
  SlackUserEvent, SlackTeam, SlackConversation, SlackConversationQuery, SlackConversationQueryRun
from application.initialize.db_init import db
from datetime import datetime
from slack.errors import SlackApiError

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
        event_datetime = datetime.utcfromtimestamp(raw_event_json.get('event_time'))
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

def capture_slack_conversations():
  slack_teams = SlackTeam.query.all()
  for slack_team in slack_teams:
    slack_users = slack_team.slack_users()
    for slack_user in slack_users:
      new_conversation_count = 0
      updated_conversation_count = 0
      if slack_user.is_authenticated:
        slack_user_client = slack_user.slack_client()
        slack_user_conversations = _capture_raw_slack_user_conversations(slack_user_client)
        conversation_slack_api_ids = [convo['id'] for convo in slack_user_conversations]
        existing_conversations = SlackConversation.query.filter(
          (SlackConversation.slack_conversation_api_id.in_(conversation_slack_api_ids)) & \
          (SlackConversation.slack_team_id == slack_team.id)
        ).all()
        existing_conversation_ids = [convo.slack_conversation_api_id for convo in existing_conversations]
        for slack_conversation in slack_user_conversations:
          conversation_type = _get_conversation_type_from_raw_slack_conversation(slack_conversation)
          conversation_slack_api_id = slack_conversation['id']
          conversation_name = slack_conversation.get('name')
          is_deleted = slack_conversation.get('is_archived')
          if slack_conversation['id'] not in existing_conversation_ids:
            new_conversation = SlackConversation(
              slack_conversation_api_id=conversation_slack_api_id, \
              conversation_type=conversation_type, \
              conversation_name=conversation_name, \
              is_deleted=is_deleted,
              slack_team_id=slack_team.id,
              last_updated=datetime.utcnow()
            )
            db.session.add(new_conversation)
            new_conversation_count += 1
          else:
            existing_conversation = list(filter(lambda convo: convo.slack_conversation_api_id == slack_conversation['id'], existing_conversations))[0]
            update_dict = dict(conversation_type=conversation_type, conversation_name=conversation_name, is_deleted=is_deleted)
            existing_conversation.update(update_dict)
            updated_conversation_count += 1
        db.session.commit()
      print('Added %s new slack_conversations to DB and updated %s slack_conversations for the SlackUser with ID: %s' % (new_conversation_count, updated_conversation_count, slack_user.id))
        # print something about running job

def capture_slack_conversation_queries():
  slack_teams = SlackTeam.query.all()
  for slack_team in slack_teams:
    slack_conversations = slack_team.slack_conversations()
    slack_users = slack_team.slack_users()
    for slack_user in slack_users:
      new_conversation_query_count = 0
      slack_conversation_query_run = SlackConversationQueryRun(query_start_time=datetime.utcnow(), slack_user_id=slack_user.id)
      slack_conversation_query_run.save()
      slack_client = slack_user.slack_client()
      for slack_conversation in slack_conversations:
        try:
          conversation_info = slack_client.conversations_info(channel=slack_conversation.slack_conversation_api_id).data.get('channel')
          if conversation_info.get('is_member') or conversation_info.get('last_read'):
            last_read_string = conversation_info.get('last_read')
            last_read = datetime.utcfromtimestamp(int(float(last_read_string))) if last_read_string else None

            new_conversation_query = SlackConversationQuery(
              slack_user_id=slack_user.id,
              slack_conversation_id=slack_conversation.id,
              query_datetime=datetime.utcnow(),
              last_read_datetime=last_read,
              last_updated=datetime.utcnow(),
              slack_conversation_query_run_id=slack_conversation_query_run.id
            )
            db.session.add(new_conversation_query)
            new_conversation_query_count += 1
        except SlackApiError as e:
          continue
      slack_conversation_query_run.query_end_time=datetime.utcnow()
      db.session.commit()
      print('For user w/ ID: %s, %s new SlackConversationQuery rows were created' % (slack_user.id, new_conversation_query_count))

# Tested using a limit to check the loop, it works
def _capture_raw_slack_user_conversations(slack_user_client):
  channel_types_str = str.join(', ', ['public_channel', 'private_channel', 'im', 'mpim'])
  next_cursor = ''
  result = slack_user_client.conversations_list(types=channel_types_str).data
  raw_user_conversations = result.get('channels')
  next_cursor = result.get('response_metadata').get('next_cursor')
  while next_cursor != '':
    result = slack_user_client.conversations_list(types=channel_types_str, cursor=next_cursor).data
    raw_user_conversations = raw_user_conversations + result.get('channels')
    next_cursor = result.get('response_metadata').get('next_cursor')
  return raw_user_conversations

def _get_conversation_type_from_raw_slack_conversation(raw_slack_conversation):
  is_private = raw_slack_conversation.get('is_private')
  is_im = raw_slack_conversation.get('is_im')
  is_mpim = raw_slack_conversation.get('is_mpim')
  is_channel = raw_slack_conversation.get('is_channel')
  is_group = raw_slack_conversation.get('is_group')

  if is_mpim: return 'mpim'
  if is_im: return 'im'
  if is_channel: return 'public_channel'
  if (is_group and is_private): return 'private_channel'
  
  print('Not sure what conversation type this is: %s' % raw_slack_conversation.get('id'))
  return None

