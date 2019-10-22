from flask import redirect, url_for
from application import application


import functools

SLACK_INSTALL_ROUTE = '/slack-install'
SLACK_AUTH_ROUTE = '/slack-authorize'
NGROK = 'https://2f72c0ee.ngrok.io'
# SLACK_AUTH_URL = NGROK + SLACK_AUTH_ROUTE
REDIRECT_URI = ''
TEST_SLACK_CLIENT_ID = '557358026116.693643634144'

SLACK_SCOPES = [
  'channels:history',
  'channels:read',
  #'conversations:list',
  #'conversations:read',
  'dnd:read',
  'groups:history',
  'groups:read',
  'dnd:write',
  'dnd:read',
  'groups:history',
  'groups:read',
  # 'identity',
  # 'identity.email:read:user',
  # 'identity:read:user',
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
  return '200'
  # It should then redirect back to our app IDEALLY

@application.route(SLACK_INSTALL_ROUTE)
def slack_install_route():
  print('HIT SLACK INSTALL ROUTE')
  slack_url = _build_slack_access_request()
  return redirect(slack_url)


def _build_slack_access_request():
  scope = '%s' % functools.reduce(lambda one, two: one + ',' + two, SLACK_SCOPES)
  client_id = TEST_SLACK_CLIENT_ID
  
  redirect_uri = NGROK + SLACK_AUTH_ROUTE
  return 'https://slack.com/oauth/authorize?scope=%s&client_id=%s' % (scope, client_id)


