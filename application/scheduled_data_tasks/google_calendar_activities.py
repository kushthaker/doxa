from application.google_auth import *
from application.models import GoogleCalendarEvent, GoogleCalendarUser, User
import google.auth.transport.requests

def update_google_calendar_events():
	"""
	Reflect newly added calendar events and changes to existing calendar events   
	"""
	users = GoogleCalendarUser.query.all()

	updated_events = 0
	added_events = 0

	for user in users:
		credentials = google.oauth2.credentials.Credentials(**get_credentials_dict(user))

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
						elif event.get('start').get('date'):
							s_dt = parser.parse(event.get('start').get('date'))
							e_dt = parser.parse(event.get('end').get('date'))

						existing_event.start_time = s_dt.astimezone(pytz.UTC)
						existing_event.end_time = e_dt.astimezone(pytz.UTC)

						existing_event.summary = event.get('summary')
						existing_event.description = event.get('description')
						existing_event.organizer_email = event.get('organizer').get('email')
						existing_event.organizer_self = event.get('organizer').get('self')
						existing_event.json_data = json.dumps(event)
						existing_event.updated_at = datetime.datetime.utcnow()
						existing_event.google_calendar_user_id = user.id

						existing_event.save()
						updated_events += 1
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
						new_event.json_data = json.dumps(event)
						new_event.google_calendar_user_id = user.id

						db.session.add(new_event)
						db.session.commit()
						added_events += 1
			except RefreshError as e:
				print("Error with google_calendar_activities.update_google_calendar_events.")
				print(e)
				continue
			except Exception as e:
				print("Error with google_calendar_activities.update_google_calendar_events.")
				print(e)
				continue
	print("Inserted ", added_events, \
		" and updated ", updated_events, \
		" GoogleCalendarEvents for ", len(users), \
		" users.")			
	
	return

def delete_google_calendar_events():
	"""
	Reflect when upcoming calendar events are deleted.  
	"""
	users = GoogleCalendarUser.query.all()

	deleted_events = 0
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
		tz = pytz.timezone(event.google_calendar_user.primary_timeZone)
		
		if ((dt_now.astimezone(tz) - dt_c.astimezone(tz)).seconds/3600 < 12) or ((dt_now.astimezone(tz) - dt_u.astimezone(tz)).seconds/3600 < 12):
			last_updated_event_ids.append(event.google_id)

	for user in users:
		credentials = google.oauth2.credentials.Credentials(**get_credentials_dict(user))

		if credentials.expired is False and credentials.valid is True:
			service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
			try:
				upcoming_event_ids = []
				events = get_upcoming_events(service)
				for event in events:
					upcoming_event_ids.append(event.get('id'))
					
				event_ids_to_delete = list(set(last_updated_event_ids).difference(set(upcoming_event_ids)))

				for event_id in event_ids_to_delete:
					GoogleCalendarEvent.query.filter(GoogleCalendarEvent.google_id == event_id).delete()
					deleted_events += 1	
			except RefreshError as e:
				print("Error with google_calendar_activities.delete_google_calendar_events.")
				print(e)
				continue
			except Exception as e:
				print("Error with google_calendar_activities.delete_google_calendar_events.")
				print(e)
				continue

	print("Deleted ", deleted_events, \
		" GoogleCalendarEvents for ", len(users), \
		" users.")			
	
	return

def get_upcoming_events(service):
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=20, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])

	if not events:
		print('No upcoming events found.')

	return events