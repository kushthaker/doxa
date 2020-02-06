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
from flask_login import login_required
from application.forms import GoogleCalendarAuthorizationForm
import urllib
from flask import request

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
		flow.redirect_uri = flask.url_for("finalize_google_auth", _external=True)
		flow.autogenerate_code_verifier = True
		authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true', prompt='consent')
		flask.session['state'] = state
		flask.session['code_verifier'] = flow.code_verifier
		return flask.redirect(authorization_url)

@application.route('/%s' % GOOGLE_CALENDAR_CALLBACK_ROUTE, methods=['GET'])
@login_required
def finalize_google_auth():
	code = request.values.get('code')
	state = flask.session.get('state')
	#code = flask.session.get('code')
	code_verifier = flask.session.get('code_verifier')

	print('in google callback')
	# cleans up stuff from session after auth
	flask.session['state'], flask.session['code'], flask.session['code_verifier'] = None, None, None

	if (code is not None) & (code_verifier is not None):
		flow = Flow.from_client_config(CLIENT_JSON, scopes=SCOPES, state=state)
		flow.redirect_uri = flask.url_for('finalize_google_auth', _external=True)
		flow.fetch_token(code=code, code_verifier=code_verifier)

		credentials = flow.credentials
		current_google_calendar_user = current_user.google_calendar_user		
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

	return flask.redirect('/app#/settings')

def credentials_to_dict(credentials):
	return {
		'token': credentials.token,
		'refresh_token': credentials.refresh_token,
		'token_uri': credentials.token_uri,
		'scopes': credentials.scopes
	}

def args_to_url_params(**kwargs):
	return urllib.parse.urlencode(dict(kwargs))

def get_credentials_dict(user):
	return {
		'token': user.auth_token,
		'refresh_token': user.refresh_token,
		'token_uri': 'https://oauth2.googleapis.com/token',
		'client_id': GOOGLE_CLIENT_ID,
		'client_secret': GOOGLE_CLIENT_SECRET,
		'scopes': fix_scopes_string(user.scopes)
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

def fix_scopes_string(scopes):
	if len(scopes) < 2:
		return scopes
	return list(map(lambda x: x[1:-1], scopes[1:-1].split(', ')))