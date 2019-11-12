# steps https://developers.google.com/identity/protocols/OAuth2WebServer
import flask
from application import application
import os
import datetime
import requests
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# CLIENT_SECRETS_FILE = 'client_secret.json'
# TEMP
CLIENT_SECRET = {"web":{"client_id":"1057982365001-4u1afil0q973df5h081sj09o8kelcesn.apps.googleusercontent.com","project_id":"doxa-258723","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"_9492CqguE3T1j_Zu3mpQSeJ"}}
GOOGLE_CALENDAR_AUTH_ROUTE = '/google_calendar_auth'

SCOPES = [
'https://www.googleapis.com/auth/calendar',
'https://www.googleapis.com/auth/calendar.events',
'https://www.googleapis.com/auth/calendar.settings.readonly']

API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

@application.route('/test')
def test_api_request():
	if 'credentials' not in flask.session:
		return flask.redirect(GOOGLE_CALENDAR_AUTH_ROUTE)
	credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
	service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	print('Getting the upcoming 10 events')
	events_result = service.events().list(calendarId='primary', timeMin=now,
		maxResults=10, singleEvents=True,
		orderBy='startTime').execute()
	events = events_result.get('items', [])
	if not events:
		print('No upcoming events found.')

	for event in events:
			start = event['start'].get('dateTime', event['start'].get('date'))
			print(start, event['summary'])

	# Save credentials back to session in case access token was refreshed.
	# ACTION ITEM: In a production app, you likely want to save these
	#              credentials in a persistent database instead.
	flask.session['credentials'] = credentials_to_dict(credentials)

	return flask.jsonify(events)

@application.route(GOOGLE_CALENDAR_AUTH_ROUTE)
def google_calendar_auth_route():
  	flow = google_auth_oauthlib.flow.Flow.from_client_config(CLIENT_SECRET, scopes=SCOPES)
  	flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
  	authorization_url, state = flow.authorization_url(
      # Enable offline access so that you can refresh an access token without
      # re-prompting the user for permission. Recommended for web server apps.
      access_type='offline',
      # Enable incremental authorization. Recommended as a best practice.
      include_granted_scopes='true')
  	flask.session['state'] = state
  	return flask.redirect(authorization_url)

@application.route('/oauth2callback')
def oauth2callback():
  		state = flask.session['state']
  		flow = google_auth_oauthlib.flow.Flow.from_client_config(CLIENT_SECRET, scopes=SCOPES, state=state)
  		flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  		authorization_response = flask.request.url
  		flow.fetch_token(authorization_response=authorization_response)
  		credentials = flow.credentials
  		flask.session['credentials'] = credentials_to_dict(credentials)
  		return flask.redirect(flask.url_for('test_api_request'))


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

