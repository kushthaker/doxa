# steps https://developers.google.com/identity/protocols/OAuth2WebServer
import flask
from application import application
import os
import datetime
import pytz
from dateutil import parser
import requests
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery


import pdb

GOOGLE_CLIENT_ID = application.config['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = application.config['GOOGLE_CLIENT_SECRET']
CLIENT_JSON = {"web":{"client_id":GOOGLE_CLIENT_ID,"project_id":"doxa-258723","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":GOOGLE_CLIENT_SECRET}}

GOOGLE_CALENDAR_AUTH_ROUTE = 'build_google_calendar_auth_request'
GOOGLE_CALENDAR_CALLBACK_ROUTE = 'google_calendar_oauth2callback'

SCOPES = [
'https://www.googleapis.com/auth/calendar',
'https://www.googleapis.com/auth/calendar.events',
'https://www.googleapis.com/auth/calendar.settings.readonly'
]

API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

def get_free_times(events):

	free_times = []
	m_interrupts = []

	for event in events:
		st = parser.parse(event.get('start').get('dateTime'))
		et = parser.parse(event.get('end').get('dateTime'))
		title = event.get('summary')
		m_interrupts.append({'start':st.replace(tzinfo=pytz.UTC),'end':et.replace(tzinfo=pytz.UTC),'title':title})

	free_start = datetime.datetime(m_interrupts[0].get('start').year, m_interrupts[0].get('start').month, m_interrupts[0].get('start').day, 8, 00, 00, tzinfo=pytz.UTC)
	free_end = datetime.datetime(m_interrupts[0].get('end').year, m_interrupts[0].get('end').month, m_interrupts[0].get('end').day, 18, 00, 00, tzinfo=pytz.UTC)

	for i in range(len(m_interrupts)-1):
		start_block = {'start':free_start,'end':m_interrupts[i].get('start')}
		if free_start.date() == m_interrupts[i+1].get('start').date():
			free_times.append(start_block)
			free_times.append({'start':m_interrupts[i].get('end'),'end':m_interrupts[i+1].get('start')})
			free_times.append({'start':m_interrupts[i+1].get('end'),'end':free_end})
		else:
			free_times.append(start_block)
			free_times.append({'start':m_interrupts[i].get('end'),'end':free_end})
			free_start = datetime.datetime(m_interrupts[i+1].get('start').year, m_interrupts[i+1].get('start').month, m_interrupts[i+1].get('start').day, 8, 00, 00, tzinfo=pytz.UTC)
			free_end = datetime.datetime(m_interrupts[i+1].get('end').year, m_interrupts[i+1].get('end').month, m_interrupts[i+1].get('end').day, 18, 00, 00, tzinfo=pytz.UTC)

	for time in free_times:
		print(time.get('start').strftime("%c"))
		print(time.get('end').strftime("%c"))
		print("\n")


@application.route('/test')
def test_api_request():
	if 'credentials' not in flask.session:
		return flask.redirect(GOOGLE_CALENDAR_AUTH_ROUTE)
	
	#Build Calendar service from credentials
	credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
	service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

	#Get 10 upcoming events
	events_result = service.events().list(calendarId='primary', timeMin=now,
		maxResults=10, singleEvents=True,
		orderBy='startTime').execute()
	
	events = events_result.get('items', [])
	if not events:
		print('No upcoming events found.')

	get_free_times(events)

	# Save credentials back to session in case access token was refreshed.
	# ACTION ITEM: In a production app, you likely want to save these
	#              credentials in a persistent database instead.
	flask.session['credentials'] = credentials_to_dict(credentials)
	
	# return flask.render_template('calendar.html', events=events)
	return flask.jsonify(events)

@application.route('/%s' %GOOGLE_CALENDAR_AUTH_ROUTE)
def build_google_calendar_auth_request():
		flow = google_auth_oauthlib.flow.Flow.from_client_config(CLIENT_JSON, scopes=SCOPES)
		flow.redirect_uri = flask.url_for(GOOGLE_CALENDAR_CALLBACK_ROUTE, _external=True)
		authorization_url, state = flow.authorization_url(
			# Enable offline access so that you can refresh an access token without
			# re-prompting the user for permission. Recommended for web server apps.
			access_type='offline',
			# Enable incremental authorization. Recommended as a best practice.
			include_granted_scopes='false')
		flask.session['state'] = state
		return flask.redirect(authorization_url)

@application.route('/%s' %GOOGLE_CALENDAR_CALLBACK_ROUTE)
def google_calendar_oauth2callback():
			state = flask.session['state']
			flow = google_auth_oauthlib.flow.Flow.from_client_config(CLIENT_JSON, scopes=SCOPES, state=state)
			flow.redirect_uri = flask.url_for(GOOGLE_CALENDAR_CALLBACK_ROUTE, _external=True)

			authorization_response = flask.request.url
			flow.fetch_token(authorization_response=authorization_response)
			credentials = flow.credentials
			flask.session['credentials'] = credentials_to_dict(credentials)

			return flask.redirect(flask.url_for('test_api_request'))

@application.route('/revoke')
def revoke():
  if 'credentials' not in flask.session:
    return ('You need to <a href="/authorize">authorize</a> before ' +
            'testing the code to revoke credentials.')

  credentials = google.oauth2.credentials.Credentials(
    **flask.session['credentials'])

  revoke = requests.post('https://accounts.google.com/o/oauth2/revoke',
      params={'token': credentials.token},
      headers = {'content-type': 'application/x-www-form-urlencoded'})

  status_code = getattr(revoke, 'status_code')
  if status_code == 200:
    return('Credentials successfully revoked.' + print_index_table())
  else:
    return('An error occurred.' + print_index_table())

@application.route('/clear')
def clear_credentials():
	if 'credentials' in flask.session:
		del flask.session['credentials']
	return ('Credentials have been cleared.<br><br>' +
					print_index_table())

def credentials_to_dict(credentials):
	return {'token': credentials.token,
					'refresh_token': credentials.refresh_token,
					'token_uri': credentials.token_uri,
					'client_id': credentials.client_id,
					'client_secret': credentials.client_secret,
					'scopes': credentials.scopes}

def print_index_table():
	return ('<table>' +
					'<tr><td><a href="/test">Test an API request</a></td>' +
					'<td>Submit an API request and see a formatted JSON response. ' +
					'    Go through the authorization flow if there are no stored ' +
					'    credentials for the user.</td></tr>' +
					'<tr><td><a href="/authorize">Test the auth flow directly</a></td>' +
					'<td>Go directly to the authorization flow. If there are stored ' +
					'    credentials, you still might not be prompted to reauthorize ' +
					'    the application.</td></tr>' +
					'<tr><td><a href="/revoke">Revoke current credentials</a></td>' +
					'<td>Revoke the access token associated with the current user ' +
					'    session. After revoking credentials, if you go to the test ' +
					'    page, you should see an <code>invalid_grant</code> error.' +
					'</td></tr>' +
					'<tr><td><a href="/clear">Clear Flask session credentials</a></td>' +
					'<td>Clear the access token currently stored in the user session. ' +
					'    After clearing the token, if you <a href="/test">test the ' +
					'    API request</a> again, you should go back to the auth flow.' +
					'</td></tr></table>')

