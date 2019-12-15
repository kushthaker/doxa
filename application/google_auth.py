import os
import flask
from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from application.models import GoogleCalendarUser, GoogleCalendarEvent
from flask_login import login_user, current_user, logout_user, login_required
import datetime
import pytz
from dateutil import parser
import requests
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import ipdb

GOOGLE_CLIENT_ID = Config.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = Config.GOOGLE_CLIENT_SECRET

CLIENT_JSON = {"web":{"client_id":GOOGLE_CLIENT_ID,"project_id":"doxa-258723","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":GOOGLE_CLIENT_SECRET}}

GOOGLE_CALENDAR_AUTH_ROUTE = 'build_google_calendar_auth_request'
GOOGLE_CALENDAR_CALLBACK_ROUTE = 'google_calendar_oauth2callback'

API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

SCOPES = [
'https://www.googleapis.com/auth/calendar',
'https://www.googleapis.com/auth/calendar.events',
'https://www.googleapis.com/auth/calendar.settings.readonly'
]

def get_upcoming_events(service):
	# Upcoming 10 Events
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=20, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])
	if not events:
		print('No upcoming events found.')
	return events

def save_upcoming_events(events):
	for event in events:
		existing_event = GoogleCalendarEvent.query.filter(GoogleCalendarEvent.google_id == event.get('id')).one_or_none()
		if existing_event:
			if event.get('start').get('dateTime'):
				s_dt = parser.parse(event.get('start').get('dateTime'))
				e_dt = parser.parse(event.get('end').get('dateTime'))
			elif event.get('start').get('date'):
				s_dt = parser.parse(event.get('start').get('date'))
				e_dt = parser.parse(event.get('end').get('date'))

			existing_event.start_time = s_dt.astimezone(pytz.UTC)
			existing_event.end_time = e_dt.astimezone(pytz.UTC)

			existing_event.summary = event.get('summary')
			existing_event.description = event.get('description')
			existing_event.organizer_email = event.get('organizer').get('email')
			existing_event.organizer_self = event.get('organizer').get('self')
			existing_event.attendees = str(event.get('attendees'))
			existing_event.conference_data = str(event.get('conferenceData'))

			existing_event.updated_at = datetime.datetime.utcnow()

			existing_event.user_id = current_user.id
			existing_event.google_user_id = current_user.google_calendar_users.id

			existing_event.save()
		else:
			new_event = GoogleCalendarEvent()
			new_event.google_id = event.get('id')
			new_event.ical_uid = event.get('iCalUID')

			if event.get('start').get('dateTime'):
				s_dt = parser.parse(event.get('start').get('dateTime'))
				e_dt = parser.parse(event.get('end').get('dateTime'))
			elif event.get('start').get('date'):
				s_dt = parser.parse(event.get('start').get('date'))
				e_dt = parser.parse(event.get('end').get('date'))

			new_event.start_time = s_dt.astimezone(pytz.UTC)
			new_event.end_time = e_dt.astimezone(pytz.UTC)

			new_event.summary = event.get('summary')
			new_event.description = event.get('description')
			new_event.organizer_email = event.get('organizer').get('email')
			new_event.organizer_self = event.get('organizer').get('self')
			new_event.attendees = str(event.get('attendees'))
			new_event.conference_data = str(event.get('conferenceData'))
			new_event.user_id = current_user.id
			new_event.google_user_id = current_user.google_calendar_users.id

			db.session.add(new_event)
			db.session.commit()
	return True

@login_required
@application.route('/google-auth')
def request_api():
	if 'credentials' not in flask.session:
		return flask.redirect(GOOGLE_CALENDAR_AUTH_ROUTE)

	#Build Calendar service from credentials
	credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
	
	if credentials.refresh_token == None:
		user = GoogleCalendarUser.query.first()
		credentials = google.oauth2.credentials.Credentials(**get_credentials_dict())
		service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
	else:
		service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

	calendarList = service.calendarList().list().execute() 
	primaryCal = next((filter(lambda cal: (cal.get('primary') == True), calendarList.get('items'))))

	existing_user = GoogleCalendarUser.query.filter(GoogleCalendarUser.google_email == primaryCal.get('id')).one_or_none()

	if existing_user:
		existing_user.auth_token = credentials.token
		existing_user.refresh_token = credentials.refresh_token
		existing_user.scopes = str(credentials.scopes)
		existing_user.primary_timeZone = primaryCal.get('timeZone')
		existing_user.primary_etag = primaryCal.get('etag')
		existing_user.primary_color_id = primaryCal.get('colorId')
		existing_user.user_id = current_user.id
		existing_user.updated_at = datetime.datetime.utcnow()
		existing_user.save()
	else:
		new_user = GoogleCalendarUser()
		new_user.google_email = primaryCal.get('id')
		new_user.auth_token = credentials.token
		new_user.refresh_token = credentials.refresh_token
		new_user.scopes = str(credentials.scopes)
		new_user.primary_timeZone = primaryCal.get('timeZone')
		new_user.primary_etag = primaryCal.get('etag')
		new_user.primary_color_id = primaryCal.get('colorId')
		new_user.user_id = current_user.id
		db.session.add(new_user)
		db.session.commit()

	# Save credentials back to session in case access token was refreshed.
	# ACTION ITEM: In a production app, you likely want to save these
	#              credentials in a persistent database instead.
	flask.session['credentials'] = credentials_to_dict(credentials)

	try: 
		save_upcoming_events(get_upcoming_events(service))
		print('events successfully saved')
	except:
		print('error with save_upcoming_events(get_upcoming_events(service))')
	finally:
		save_upcoming_events(get_upcoming_events(service))
	
	return flask.jsonify(get_upcoming_events(service))

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

	return flask.redirect(flask.url_for('request_api'))

@application.route('/revoke-google-auth')
def revoke_google_auth():
	if 'credentials' not in flask.session:
		return ('No credentials in session. You need to <a href="/google-auth">authorize</a>.')

	credentials = google.oauth2.credentials.Credentials(**flask.session['credentials'])
	revoke = requests.post('https://accounts.google.com/o/oauth2/revoke', 
		params={'token': credentials.token}, 
		headers = {'content-type': 'application/x-www-form-urlencoded'})

	status_code = getattr(revoke, 'status_code')

	if status_code == 200:
		return('Credentials successfully revoked.')
	else:
		return('Error with revoke post request to https://accounts.google.com/o/oauth2/revoke.')

@application.route('/clear-google-auth')
def clear_google_auth():
	if 'credentials' in flask.session:
		del flask.session['credentials']
	return ('Credentials have been cleared.<br><br>')

def credentials_to_dict(credentials):
	return {'token': credentials.token,
					'refresh_token': credentials.refresh_token,
					'token_uri': credentials.token_uri,
					'client_id': credentials.client_id,
					'client_secret': credentials.client_secret,
					'scopes': credentials.scopes}

def get_credentials_dict():
	user = GoogleCalendarUser.query.filter(GoogleCalendarUser.user_id == current_user.id).first()
	return {'token': user.auth_token,
		'refresh_token': user.refresh_token,
		'token_uri': 'https://oauth2.googleapis.com/token',
		'client_id': GOOGLE_CLIENT_ID,
		'client_secret': GOOGLE_CLIENT_SECRET,
		'scopes': user.scopes}
