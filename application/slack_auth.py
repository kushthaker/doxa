from flask import redirect, request
from application import application
from application.models import SlackUser, SlackTeam
import slack
import functools
from datetime import datetime

SLACK_INSTALL_ROUTE = '/slack-install'
SLACK_AUTH_ROUTE = '/slack-auth-one'

# temp
application.config['SLACK_CLIENT_ID'] = '557358026116.693643634144'
application.config['SLACK_CLIENT_SECRET'] = '96de57cbf3469a70ee97c69f9e1d32d7'
import pdb

SLACK_CLIENT_ID = application.config['SLACK_CLIENT_ID']
SLACK_CLIENT_SECRET = application.config['SLACK_CLIENT_SECRET']

SLACK_SCOPES = [
  'channels:history',
  'channels:read',
  'dnd:read',
  'groups:history',
  'groups:read',
  'dnd:write',
  'dnd:read',
  'groups:history',
  'groups:read',
  'im:history',
  'im:read',
  'links:read',
  'mpim:read',
  'mpim:history',
  'reactions:read',
  'reminders:read',
  'reminders:write',
  'team:read',
  'usergroups:read',
  'users.profile:read',
  'users:read',
  'users:read.email'
]

@application.route(SLACK_AUTH_ROUTE)
def slack_auth_route():
  code = request.values.get('code')

  web_client = slack.WebClient()
  response = web_client.oauth_access(code=code, client_id=SLACK_CLIENT_ID, client_secret=SLACK_CLIENT_SECRET)
  res_data = response.data

  authentication_oauth_access_token = res_data.get('access_token') # this is user specific
  new_slack_team = SlackTeam(res_data)
  existing_slack_team = SlackTeam.query.filter_by(slack_team_api_id=new_slack_team.slack_team_api_id).first()

  slack_team = None
  if existing_slack_team:
    existing_slack_team.update_registration(new_slack_team)
    existing_slack_team.save()
    slack_team = existing_slack_team
  else:
    new_slack_team.save()
    slack_team = new_slack_team

  slack_user_api_id = res_data.get('user_id')
  existing_user = SlackUser.query.filter_by(slack_user_api_id=slack_user_api_id).one_or_none()

  if existing_user:
    existing_user.is_authenticated = True
    existing_user.authentication_oauth_access_token = authentication_oauth_access_token
    existing_user.save()
  else:
    web_client = build_slack_web_client_from_team(slack_team=slack_team)
    response = web_client.users_info(user=slack_user_api_id).data
    user_info_data = response.get('user')
    # THEN create Slack user from who is authenticating
    user_profile_data = user_info_data.get('profile')
    new_slack_user = SlackUser(
                               slack_user_api_id = user_info_data.get('id'), \
                               slack_team_id = slack_team.id, \
                               slack_email_address = user_profile_data.get('email'), \
                               first_name = user_profile_data.get('first_name'), \
                               last_name = user_profile_data.get('last_name'), \
                               slack_username = user_info_data.get('name'), \
                               is_authenticated = True, \
                               authentication_oauth_access_token = authentication_oauth_access_token, \
                               is_deleted_on_slack = user_info_data.get('deleted'), \
                               created_date = datetime.utcnow(), \
                               slack_timezone_label = user_info_data.get('tz_label'), \
                               slack_timezone_offset = user_info_data.get('tz_offset'), \
                               last_updated = datetime.utcnow() \
                              )
    new_slack_user.save() # will want to then send them an email to get them onboarded or something

  # this should eventually redirect to our homepage with some details on what we will do with Slack data
  return _redirect_back_to_slack(slack_team.slack_team_api_id)

@application.route(SLACK_INSTALL_ROUTE)
def slack_install_route():
  slack_url = _build_slack_access_request()
  return redirect(slack_url)

def _build_slack_access_request():
  scope = '%s' % functools.reduce(lambda one, two: one + ',' + two, SLACK_SCOPES)
  client_id = SLACK_CLIENT_ID
  return 'https://slack.com/oauth/authorize?scope=%s&client_id=%s' % (scope, client_id)

def _redirect_back_to_slack(team_id: str):
  return redirect('slack://open?team=%s' % team_id)

def build_slack_web_client_from_user(slack_user: SlackUser=None, slack_user_api_id: str=None, connection_test: bool=False):
  if slack_user is None:
    if slack_user_api_id is not None:
      slack_user = SlackUser.query.filter_by(slack_user_api_id=slack_user_api_id).one()
    else:
      raise ValueError('Must provide a SlackUser or slack_user_api_id')

  slack_api_token = slack_user.api_access_token
  client = slack.WebClient(slack_api_token)
  if connection_test:
    _test_web_slack_client(client)

  return client

def build_slack_web_client_from_team(slack_team: SlackTeam=None, slack_api_team_id: str=None, connection_test: bool=False):
  if slack_team is None:
    if slack_team_api_id is not None:
      slack_team = SlackTeam.query.filter_by(slack_team_api_id=slack_team_api_id).one()
    else:
      raise ValueError('Must provide a team or team_id')

  slack_api_token = slack_team.api_access_token
  client = slack.WebClient(slack_api_token)
  if connection_test:
    _test_web_slack_client(client)

  return client

def _test_web_slack_client(client: slack.WebClient):
  client.api_test()
  return client
