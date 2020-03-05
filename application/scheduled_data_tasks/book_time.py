from application.models import GoogleCalendarEvent, GoogleCalendarUser, User
import httplib2
import google_auth_httplib2
from google.oauth2.credentials import Credentials
from application.google_auth import get_credentials_dict
import googleapiclient.discovery
import dateutil
import json
from google.auth.exceptions import RefreshError
import pytz
from application.google_auth import API_SERVICE_NAME, API_VERSION
import datetime
from application.initialize.db_init import db

def set_utc_tz(event):
  if event.get('start').get('dateTime'):
    s_dt = dateutil.parser.parse(event.get('start').get('dateTime'))
    e_dt = dateutil.parser.parse(event.get('end').get('dateTime'))
    s_dt = s_dt.replace(tzinfo=pytz.UTC) - s_dt.utcoffset()
    e_dt = e_dt.replace(tzinfo=pytz.UTC) - e_dt.utcoffset()
  elif event.get('start').get('date'):
    s_dt = dateutil.parser.parse(event.get('start').get('date'))
    e_dt = dateutil.parser.parse(event.get('end').get('date'))
    s_dt = s_dt.replace(tzinfo=pytz.UTC)
    e_dt = e_dt.replace(tzinfo=pytz.UTC)
  event_id = event.get('summary')
  return dict({'start':s_dt,'end':e_dt,'event_id':event_id})

def get_upcoming_events(service):
  now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
  events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=100, singleEvents=True, orderBy='startTime').execute()
  events = events_result.get('items', [])
  if not events:
    print('No upcoming events found.')
  return events

def attempt_booking(start, end, g_user, service):
  focus_length = g_user.user.focus_length
  
  if end - start >= datetime.timedelta(hours=focus_length):
    event = {
    'summary': GoogleCalendarEvent.FOCUS_TIME_EVENT_SUMMARY_NAME,
    'location': 'Desk',
    'description': 'Uninterrupted time for your most important work.',
    'start': {
      'dateTime': start.isoformat(),
      'timeZone': g_user.primary_timeZone,
    },
    'end': {
      'dateTime': (start + datetime.timedelta(hours=focus_length)).isoformat(),
      'timeZone': g_user.primary_timeZone,
    },
    'colorId':'3',
    'reminders': {
      'useDefault': False,
      'overrides': [
        {'method': 'popup', 'minutes': 10},
      ],
    },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    return True
  else:
    return False

def get_user_service(g_user):
  credentials = Credentials(**get_credentials_dict(g_user))
  if credentials.expired is False and credentials.valid is True: ## other checks here?
    service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    if service:
      return service
    else:
      return False

def book_upcoming_week_focus_time():
  """
  Book time into first delta > g_user.user.focus_length over user's next 7 weekdays.

  """
  g_users = GoogleCalendarUser.query.all()

  for g_user in g_users:
      service = get_user_service(g_user)
      if service:
        events = get_upcoming_events(service)
      
      utc_events = [set_utc_tz(e) for e in events]
      
      dates = []
      for i in range(1,8):
        dates.append(datetime.datetime.utcnow().date() + datetime.timedelta(days=i))
      dates = dict.fromkeys([e for e in dates if e.weekday() not in [5,6]])
      for k,v in dates.items():
        dates[k] = [e for e in utc_events if e.get('start').date() == k]

      for k,v in dates.items():
        workday_start =  pytz.utc.localize(datetime.datetime(k.year, k.month, k.day, g_user.user.workday_start.hour, g_user.user.workday_start.minute))
        workday_end = pytz.utc.localize(datetime.datetime(k.year, k.month, k.day, g_user.user.workday_end.hour, g_user.user.workday_end.minute))
        day_events = sorted(dates[k], key= lambda i: i.get('start'))
        day_events = [d for d in day_events if (d.get('end').time() > workday_start.time()) and (d.get('start').time() < workday_end.time())]

        if len(day_events) == 0:
          attempt_booking(workday_start, workday_end, g_user, service)
          dates[k].append(dict({'focus_booked': 1}))
          continue

        if attempt_booking(workday_start, day_events[0].get('start'), g_user, service):
          dates[k].append(dict({'focus_booked': 1}))
          continue
          
        for i in range(0, len(day_events)):
          if (i+1 < len(day_events)):
            if attempt_booking(day_events[i].get('end'),day_events[i+1].get('start'), g_user, service):
              dates[k].append(dict({'focus_booked': 1}))
            break

        if dates[k][-1].get('focus_booked'):
          continue
        else:
          if attempt_booking(day_events[-1].get('end'), workday_end, g_user, service):
            dates[k].append(dict({'focus_booked': 1}))
            continue

        # logic to double book if one day too busy for focus (dates where dates[k][-1].get('focus_booked') == 0)

  print("Booked focus times for all google users.")