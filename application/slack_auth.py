from flask import redirect, request
from application import application
from application.models import SlackTeam
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
  if existing_slack_team:
    existing_slack_team.update_registration(new_slack_team)
    existing_slack_team.save()
    return _redirect_back_to_slack(existing_slack_team.slack_team_id)
  else:
    new_slack_team.save()
    return _redirect_back_to_slack(new_slack_team.slack_team_id)

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

