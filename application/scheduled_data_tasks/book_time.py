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
  event_id = event.get('id')
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
  
  if end - start > datetime.timedelta(hours=focus_length):
    event = {
    'summary': 'Focus Time',
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

def book_upcoming_week_focus_time():
  """
  Book time into first delta > g_user.user.focus_length over user's next 7 weekdays.

  """
  g_users = GoogleCalendarUser.query.all()

  for g_user in g_users:
    credentials = Credentials(**get_credentials_dict(g_user))
    if credentials.expired is False and credentials.valid is True: ## other checks here?
      service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
      events = get_upcoming_events(service)
      utc_events = [set_utc_tz(e) for e in events]
      
      dates = []
      for i in range(1,10):
        dates.append(datetime.datetime.utcnow().date() + datetime.timedelta(days=i))
      dates = dict.fromkeys([e for e in dates if e.weekday() not in [5,6]])
      for k,v in dates.items():
        dates[k] = [e for e in utc_events if e.get('start').date() == k]

      for k,v in dates.items():
        workday_start =  pytz.utc.localize(datetime.datetime(k.year, k.month, k.day, g_user.user.workday_start.hour, g_user.user.workday_start.minute))
        workday_end = pytz.utc.localize(datetime.datetime(k.year, k.month, k.day, g_user.user.workday_end.hour, g_user.user.workday_end.minute))
        day_events = sorted(dates[k], key= lambda i: i['start'])

        if attempt_booking(workday_start, day_events[0].get('start'), g_user, service):
          dates[k].append(dict({'focus_booked': 1}))
          continue
          
        for i in range(len(day_events)-1):
          if attempt_booking(day_events[i].get('end'),day_events[i+1].get('start'), g_user, service):
            dates[k].append(dict({'focus_booked': 1}))
            break
        
        if dates[k][-1].get('focus_booked'):
          continue
        else:
          if attempt_booking(day_events[-1].get('end'), workday_end, g_user, service):
            dates[k].append(dict({'focus_booked': 1}))
            continue

        dates[k].append(dict({'focus_booked': 0}))

  print("Booked focus times for all google users")

"""
Utility functions for Google API
"""

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


# def get_credentials_dict(user):
#   return {
#     'token': user.auth_token,
#     'refresh_token': user.refresh_token,
#     'token_uri': 'https://oauth2.googleapis.com/token',
#     'client_id': GOOGLE_CLIENT_ID,
#     'client_secret': GOOGLE_CLIENT_SECRET,
#     'scopes': fix_scopes_string(user.scopes)
#   }

