import flask
from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from application.models import GoogleCalendarUser, GoogleCalendarEvent, User
from flask_login import login_user, current_user, logout_user, login_required
import datetime
import pytz
from dateutil import parser
import requests
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import googleapiclient.discovery
from google.auth.exceptions import RefreshError
from application.utils.route_utils import token_required
from application.forms import GoogleCalendarAuthorizationForm
import urllib

GOOGLE_CLIENT_ID = Config.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = Config.GOOGLE_CLIENT_SECRET

CLIENT_JSON = {"web":{"client_id":GOOGLE_CLIENT_ID,"project_id":"doxa-258723","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":GOOGLE_CLIENT_SECRET}}

GOOGLE_CALENDAR_INITIAL_AUTHENTICATION_ROUTE = 'google-auth'
GOOGLE_CALENDAR_AUTH_ROUTE = 'build_google_calendar_auth_request'
GOOGLE_CALENDAR_CALLBACK_ROUTE = 'google_calendar_oauth2callback'

API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

SCOPES = [ 'https://www.googleapis.com/auth/calendar',
'https://www.googleapis.com/auth/calendar.events',
'https://www.googleapis.com/auth/calendar.settings.readonly']

def update_existing_user_creds(existing_user, credentials, primaryCal, current_user):
	existing_user.auth_token = credentials.token
	existing_user.refresh_token = credentials.refresh_token if credentials.refresh_token else existing_user.refresh_token
	existing_user.scopes = str(credentials.scopes)
	existing_user.primary_timeZone = primaryCal.get('timeZone')
	existing_user.primary_etag = primaryCal.get('etag')
	existing_user.primary_color_id = primaryCal.get('colorId')
	existing_user.user_id = current_user.id
	existing_user.updated_at = datetime.datetime.utcnow()
	existing_user.save()
	return existing_user

def add_new_user_creds(credentials, primaryCal, current_user):
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
	return new_user

@application.route('/%s' % GOOGLE_CALENDAR_INITIAL_AUTHENTICATION_ROUTE)
@login_required
def request_google_calendar_api():
	if 'credentials' not in flask.session:
		print('credentials not in flask session')
		return flask.redirect(GOOGLE_CALENDAR_AUTH_ROUTE)

	credentials = Credentials(**flask.session['credentials'])
	if credentials.expired is False and credentials.valid is True:
		service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
		try:
			calendarList = service.calendarList().list().execute()
			primaryCal = next((filter(lambda cal: (cal.get('primary') == True), calendarList.get('items'))))
		except RefreshError as e:
			print(e)
			del flask.session['credentials']
			return flask.redirect(GOOGLE_CALENDAR_AUTH_ROUTE)
	else:
		flask.flash('Google account is not authorized.', 'danger')
		return flask.redirect(flask.url_for('home'))
	
	if current_user.google_calendar_user:
		existing_user = GoogleCalendarUser.query.filter(GoogleCalendarUser.id == current_user.google_calendar_user.id).one_or_none()
		user = update_existing_user_creds(existing_user, credentials, primaryCal, current_user)
	else:
		user = add_new_user_creds(credentials, primaryCal, current_user)

	return flask.jsonify(get_credentials_dict(user))

@application.route('/%s' % GOOGLE_CALENDAR_AUTH_ROUTE)
def build_google_calendar_auth_request():
		flow = Flow.from_client_config(CLIENT_JSON, scopes=SCOPES)
		flow.redirect_uri = flask.url_for(GOOGLE_CALENDAR_CALLBACK_ROUTE, _external=True)
		
		authorization_url, state = flow.authorization_url(
			access_type='offline',
			include_granted_scopes='true',
			prompt='consent')

		flask.session['state'] = state
		
		return flask.redirect(authorization_url)

@application.route('/%s' % GOOGLE_CALENDAR_CALLBACK_ROUTE)
def google_calendar_oauth2callback():
	
	state = flask.session['state']
	flow = Flow.from_client_config(CLIENT_JSON, scopes=SCOPES, state=state)
	flow.redirect_uri = flask.url_for(GOOGLE_CALENDAR_CALLBACK_ROUTE, _external=True)

	authorization_response = flask.request.url
	flow.fetch_token(authorization_response=authorization_response)
	credentials = flow.credentials

	flask.session['credentials'] = credentials_to_dict(credentials)
	url_credentials = credentials_to_url_params(credentials)
	return flask.redirect('/app#/google-auth?%s' % url_credentials)
	
@application.route('/revoke-google-auth')
def revoke_google_auth():
	if 'credentials' not in flask.session:
		return ('No credentials in session. You need to <a href="/google-auth">authorize</a>.')

	credentials = Credentials(**flask.session['credentials'])
	revoke = requests.post('https://accounts.google.com/o/oauth2/revoke', 
		params={'token': credentials.token}, 
		headers = {'content-type': 'application/x-www-form-urlencoded'})
	status_code = getattr(revoke, 'status_code')

	if status_code == 200:
		user = GoogleCalendarUser.query.filter(current_user.google_calendar_user.id == GoogleCalendarUser.id).one_or_none()
		if user:
			db.session.delete(user)
			db.session.commit()
		return('Credentials successfully revoked. Deleted current GoogleCalendarUser and child GoogleCalendarEvents.')
	else:
		return('Error with revoke post request to https://accounts.google.com/o/oauth2/revoke.')

@application.route('/clear-google-auth')
def clear_google_auth():
	if 'credentials' in flask.session:
		del flask.session['credentials']
	return ('Credentials have been cleared.<br><br>')


@application.route('/api/finalize-google-auth', methods=['POST'])
@token_required
def finalize_google_auth(current_user):
	auth_form = GoogleCalendarAuthorizationForm()
	if auth_form.validate_on_submit():
		current_google_calendar_user = current_user.google_calendar_user		
		credentials = Credentials(**auth_form.to_dict(),
	                              client_id=GOOGLE_CLIENT_ID,
	                              client_secret=GOOGLE_CLIENT_SECRET)
		primary_calendar = get_primary_calendar_details(credentials)
		if primary_calendar:
			if current_google_calendar_user:
				update_existing_user_creds(current_google_calendar_user, credentials, \
				                           primary_calendar, current_user)
			else:
				add_new_user_creds(credentials, primary_calendar, current_user)
		else:
			raise KeyError('Could not access a primary calendar for user %s' % current_user.id)
	else:
		return flask.jsonify({ 'errors': auth_form.errors })

	return flask.jsonify(current_user.user_details())

def credentials_to_dict(credentials):
	return {
		'token': credentials.token,
		'refresh_token': credentials.refresh_token,
		'token_uri': credentials.token_uri,
		'scopes': credentials.scopes
	}

def credentials_to_url_params(credentials):
	dict_credentials = credentials_to_dict(credentials)
	return urllib.parse.urlencode(dict_credentials)

def get_credentials_dict(user):
	return {
		'token': user.auth_token,
		'refresh_token': user.refresh_token,
		'token_uri': 'https://oauth2.googleapis.com/token',
		'client_id': GOOGLE_CLIENT_ID,
		'client_secret': GOOGLE_CLIENT_SECRET,
		'scopes': user.scopes
	}

def get_primary_calendar_details(credentials):
	if credentials.expired is False and credentials.valid is True:
		service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
		try:
			calendar_list = service.calendarList().list().execute()
			primary_calendar = next((filter(lambda cal: (cal.get('primary') == True), calendar_list.get('items'))))
		except RefreshError as e:
			print(e)
			return None
		return primary_calendar
	return None
