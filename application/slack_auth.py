from flask import redirect, request
from application import application
from application.models import SlackTeam, SlackUser
import slack
import functools

SLACK_INSTALL_ROUTE = '/slack-install'
SLACK_AUTH_ROUTE = '/slack-auth-one'

# TEMP:
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
  print('HIT SLACK AUTHORIZE ROUTE')
  print(request.json)
  code = request.values.get('code')

  web_client = slack.WebClient()
  response = web_client.oauth_access(code=code, client_id=SLACK_CLIENT_ID, client_secret=SLACK_CLIENT_SECRET)
  res_data = response.data

  new_slack_team = SlackTeam(res_data)
  existing_slack_team = SlackTeam.query.filter_by(slack_team_id=new_slack_team.slack_team_id).first()

  # this should eventually redirect to our homepage with some details on what we will do with Slack data
  slack_team = None
  if existing_slack_team:
    existing_slack_team.update_registration(new_slack_team)
    existing_slack_team.save()
    slack_team = existing_slack_team
  else:
    new_slack_team.save()
    slack_team = new_slack_team
  
  user_id = res_data.get('user_id')
  existing_user = SlackUser.query.filter_by(slack_user_id=user_id).one_or_none()
  if existing_user:
    existing_user.is_authenticated = True
    existing_user.save()
  else:
    web_client = build_slack_web_client(slack_team.slack_team_id)
    user_info_data = web_client.users_info(user_id).data
    # THEN create Slack user
    new_slack_user = SlackUser()

      

  return _redirect_back_to_slack(slack_team.slack_team_id)

'''
Sample `res_data` response:
{
  'ok': True,
  'access_token': 'xoxp-557358026116-556664070576-804627092836-2b6251834f1ae1412a5a9ea8baa29efc',
  'scope': 'identify,channels:history,groups:history,im:history,mpim:history,channels:read,groups:read,im:read,mpim:read,reactions:read,reminders:read,team:read,users:read,users:read.email,usergroups:read,dnd:read,users.profile:read,reminders:write,dnd:write,links:read,calls:read',
  'user_id': 'UGCKJ22GY',
  'team_id': 'TGDAJ0S3E',
  'enterprise_id': None,
  'team_name': 'doxa',
  'warning': 'superfluous_charset',
  'response_metadata': {'warnings': ['superfluous_charset']}
}
'''

  
# It should then redirect back to our app IDEALLY

@application.route(SLACK_INSTALL_ROUTE)
def slack_install_route():
  print('HIT SLACK INSTALL ROUTE')
  slack_url = _build_slack_access_request()
  return redirect(slack_url)


def _build_slack_access_request():
  scope = '%s' % functools.reduce(lambda one, two: one + ',' + two, SLACK_SCOPES)
  client_id = SLACK_CLIENT_ID
  return 'https://slack.com/oauth/authorize?scope=%s&client_id=%s' % (scope, client_id)

def _redirect_back_to_slack(team_id):
  return redirect('slack://open?team=%s' % team_id)

def build_slack_web_client(slack_api_team=None, slack_api_team_id=None, connection_test=False):
  if slack_api_team is None:
    if slack_api_team_id is not None:
      slack_api_team = SlackTeam.query.filter_by(slack_team_id=slack_api_team_id).one()
    else:
      raise ValueError('Must provide a team or team_id')
  slack_api_token = slack_api_team.api_access_token
  client = slack.WebClient(slack_api_token)
  if connection_test:
    try:
      client.api_test()
    except SlackApiError:
      print('Error: Slack Client API Key for team ID %s, Slack team ID not working' % (slack_api_team.id, slack_api_team.slack_team_id))
  return client
