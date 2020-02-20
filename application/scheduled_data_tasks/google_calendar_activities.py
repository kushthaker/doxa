from application.models import GoogleCalendarEvent, GoogleCalendarUser, User
import httplib2
import google_auth_httplib2
from google.oauth2.credentials import Credentials
from application.google_auth import get_credentials_dict
import googleapiclient.discovery
from dateutil import parser
import json
from google.auth.exceptions import RefreshError
import pytz
from application.google_auth import API_SERVICE_NAME, API_VERSION
import datetime
from application.initialize.db_init import db

def update_google_calendar_events():
	"""
	Reflect newly added calendar events and changes to existing calendar events   
	"""
	g_users = GoogleCalendarUser.query.all()

	updated_events = 0
	added_events = 0

	for g_user in g_users:
		credentials = Credentials(**get_credentials_dict(g_user))
		if credentials.expired is False and credentials.valid is True:
			service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
			try:
				events = get_upcoming_events(service)
				for event in events:
					existing_event = GoogleCalendarEvent.query.filter(GoogleCalendarEvent.google_id == event.get('id')).one_or_none()
					if existing_event:
						if event.get('start').get('dateTime'):
							s_dt = parser.parse(event.get('start').get('dateTime'))
							e_dt = parser.parse(event.get('end').get('dateTime'))
							s_dt = s_dt.replace(tzinfo=pytz.UTC) - s_dt.utcoffset()
							e_dt = e_dt.replace(tzinfo=pytz.UTC) - e_dt.utcoffset()
						elif event.get('start').get('date'):
							s_dt = parser.parse(event.get('start').get('date'))
							e_dt = parser.parse(event.get('end').get('date'))

						existing_event.start_time = s_dt
						existing_event.end_time = e_dt

						existing_event.summary = event.get('summary')
						existing_event.description = event.get('description')
						existing_event.organizer_email = event.get('organizer').get('email')
						existing_event.organizer_self = event.get('organizer').get('self')
						existing_event.json_data = json.dumps(event)
						existing_event.updated_at = datetime.datetime.utcnow()
						existing_event.google_calendar_user_id = g_user.id

						db.session.commit()
						updated_events += 1
					else:
						new_event = GoogleCalendarEvent()
						new_event.google_id = event.get('id')
						new_event.ical_uid = event.get('iCalUID')

						if event.get('start').get('dateTime'):
							s_dt = parser.parse(event.get('start').get('dateTime'))
							e_dt = parser.parse(event.get('end').get('dateTime'))
							s_dt = s_dt.replace(tzinfo=pytz.UTC) - s_dt.utcoffset()
							e_dt = e_dt.replace(tzinfo=pytz.UTC) - e_dt.utcoffset()
						elif event.get('start').get('date'):
							s_dt = parser.parse(event.get('start').get('date'))
							e_dt = parser.parse(event.get('end').get('date'))

						new_event.start_time = s_dt
						new_event.end_time = e_dt

						new_event.summary = event.get('summary')
						new_event.description = event.get('description')
						new_event.organizer_email = event.get('organizer').get('email')
						new_event.organizer_self = event.get('organizer').get('self')
						new_event.json_data = json.dumps(event)
						new_event.google_calendar_user_id = g_user.id
						
						db.session.add(new_event)
						db.session.commit()
						added_events += 1

				"""
				Delete events recently stored in DB no longer in API response.
				"""
				deleted_events = 0

				db_event_ids = get_recently_updated_events()
				res_event_ids = [e.get('id') for e in get_upcoming_events(service)]
				to_delete = list(set(db_event_ids).difference(set(res_event_ids)))

				for e_id in to_delete:
					e = GoogleCalendarEvent.query.filter(GoogleCalendarEvent.google_id == e_id)
					db.session.delete(e)
					db.session.commit()
					deleted_events += 1

				print("Inserted ", added_events, \
				" and updated ", updated_events, \
				" GoogleCalendarEvents for ", len(g_users), \
				" users.")	

				print("Deleted ", deleted_events, \
				" GoogleCalendarEvents for ", len(g_users), \
				" users.")

			except RefreshError as e:
				print("Error with google_calendar_activities.update_google_calendar_events.")
				print(e)
				continue
			except Exception as e:
				print("Error with google_calendar_activities.update_google_calendar_events.")
				print(e)
				continue
	return

def get_recently_updated_events():
	last_updated_event_ids = []
	events = GoogleCalendarEvent.query.all()

	# Get list of GoogleCalendarEvent.google_id for events updated in the last 12 hours (previous job) 
	for event in events:
		dt_c = pytz.UTC.localize(event.created_at)
		if event.updated_at:
			dt_u = pytz.UTC.localize(event.updated_at)
		else:
			dt_u = pytz.UTC.localize(datetime.datetime.utcnow())

		dt_now = pytz.UTC.localize(datetime.datetime.utcnow())
		
		if ((dt_now - dt_c).seconds/3600 < 12) or ((dt_now - dt_u).seconds/3600 < 12):
			last_updated_event_ids.append(event.google_id)
	return last_updated_event_ids

def refresh_google_credentials():
	users = GoogleCalendarUser.query.all()
	count = 0

	for user in users:
		creds_dict = get_credentials_dict(user)
		credentials = Credentials(**creds_dict)
		rq = google_auth_httplib2.Request(httplib2.Http())
		credentials.refresh(rq)
		user.auth_token = credentials.token
		db.session.add(user)
		db.session.commit()
		count += 1

	print("Updated auth token for ", count, " GoogleCalendarUsers.")

def get_upcoming_events(service):
	maxTime = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	minTime = (pytz.UTC.localize(datetime.datetime.utcnow()) - datetime.timedelta(days=200)).isoformat() 
	events_result = service.events().list(calendarId='primary', timeMin=minTime, timeMax=maxTime, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		print('No upcoming events found.')

	return events
