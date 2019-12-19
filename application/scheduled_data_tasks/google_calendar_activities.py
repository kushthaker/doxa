from application.google_auth import *
from application.models import GoogleCalendarEvent, GoogleCalendarUser, User

# CLIENT_CONFIG = {"web":{"client_id":GOOGLE_CLIENT_ID,"project_id":"doxa-258723","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":GOOGLE_CLIENT_SECRET}}
# GOOGLE_CALENDAR_AUTH_ROUTE = 'build_google_calendar_auth_request'
# GOOGLE_CALENDAR_CALLBACK_ROUTE = 'google_calendar_oauth2callback'

# API_SERVICE_NAME = 'calendar'
# API_VERSION = 'v3'

# SCOPES = [
# 'https://www.googleapis.com/auth/calendar',
# 'https://www.googleapis.com/auth/calendar.events',
# 'https://www.googleapis.com/auth/calendar.settings.readonly'
# ]

def update_user_events():
	users = GoogleCalendarUser.query.all()

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
					existing_event.google_calendar_user_id = current_user.google_calendar_user.id

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
					new_event.json_data = json.dumps(event)
					new_event.google_calendar_user_id = current_user.google_calendar_user.id

					db.session.add(new_event)
					db.session.commit()
			except:
				continue
	print("Calendar events updated.")			
	return

def get_upcoming_events(service):
	now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=20, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])
	
	if not events:
		print('No upcoming events found.')

	return events
