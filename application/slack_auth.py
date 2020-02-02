from flask import redirect, request, jsonify
import flask
from application.forms import SlackAuthorizationForm
from application.initialize.config import Config
from application.app_setup import application
from application.models import SlackTeam, SlackUser
import slack
import functools
from datetime import datetime
from flask_login import login_required, current_user
from flask import session

SLACK_INSTALL_ROUTE = '/slack-install'
SLACK_AUTH_ROUTE = '/slack-auth-one'
FINALIZE_SLACK_AUTH_ROUTE = '/api/finalize-slack-auth'
SLACK_CLIENT_ID = Config.SLACK_CLIENT_ID
SLACK_CLIENT_SECRET = Config.SLACK_CLIENT_SECRET

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
  session['code'] = request.values.get('code')
  return redirect('/app#/slack-auth')

@application.route(FINALIZE_SLACK_AUTH_ROUTE, methods=['GET'])
@login_required
def finalize_slack_auth():
  code = session['code']
  session['code'] = None
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

  user_id = res_data.get('user_id')
  existing_user = SlackUser.query.filter_by(slack_user_api_id=user_id).one_or_none()
  ret_user = None
  if existing_user:
    existing_user.user_id = current_user.id
    existing_user.is_authenticated = True
    existing_user.authentication_oauth_access_token = authentication_oauth_access_token
    existing_user.save()
    
  else:
    web_client = slack.WebClient(authentication_oauth_access_token)
    response = web_client.users_info(user=user_id).data
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
                               last_updated = datetime.utcnow(), \
                               user_id = current_user.id
                              )
    new_slack_user.save() # will want to then send them an email to get them onboarded or something

  return jsonify(current_user.user_details())

@application.route(SLACK_INSTALL_ROUTE)
def slack_install_route():
  slack_url = _build_slack_access_request()
  return redirect(slack_url)

def _build_slack_access_request():
  scope = '%s' % functools.reduce(lambda one, two: one + ',' + two, SLACK_SCOPES)
  client_id = SLACK_CLIENT_ID
  return 'https://slack.com/oauth/authorize?scope=%s&client_id=%s' % (scope, client_id)

def _redirect_back_to_slack(team_id):
  return redirect('slack://open?team=%s' % team_id)

def build_slack_web_client(slack_team=None, slack_api_team_id=None, connection_test=False):
  if slack_team is None:
    if slack_api_team_id is not None:
      slack_team = SlackTeam.query.filter_by(slack_team_id=slack_api_team_id).one()
    else:
      raise ValueError('Must provide a team or team_id')
  slack_api_token = slack_team.api_access_token
  client = slack.WebClient(slack_api_token)
  if connection_test:
    try:
      client.api_test()
    except SlackApiError:
      print('Error: Slack Client API Key for team ID %s, Slack team ID not working' % (slack_api_team.id, slack_api_team.slack_team_id))
  return client
