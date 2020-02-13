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
import pytz
from application.initialize.db_init import db


def set_utc_tz(event, g_user):
  user_tz = pytz.timezone(g_user.primary_timeZone)
  if event.get('start').get('dateTime'):
    s_dt = parser.parse(event.get('start').get('dateTime')).replace(tzinfo=pytz.UTC)
    s_dt = s_dt.astimezone(user_tz)
    e_dt = parser.parse(event.get('end').get('dateTime')).replace(tzinfo=pytz.UTC)
    e_dt = e_dt.astimezone(user_tz)
  elif event.get('start').get('date'):
    s_dt = parser.parse(event.get('start').get('date')).replace(tzinfo=pytz.UTC)
    s_dt = s_dt.astimezone(user_tz)
    e_dt = parser.parse(event.get('end').get('date')).replace(tzinfo=pytz.UTC)
    e_dt = e_dt.astimezone(user_tz)
  event_id = event.get('id')
  return dict({'start':s_dt,'end':e_dt,'event_id':event_id})

def get_upcoming_events(service):
  minTime = (pytz.UTC.localize(datetime.datetime.utcnow()) - datetime.timedelta(days=60)).isoformat() 
  events_result = service.events().list(calendarId='primary', timeMin=minTime, maxResults=200, singleEvents=True, orderBy='startTime').execute()
  events = events_result.get('items', [])
  if not events:
    print('No upcoming events found.')
  return events

def attempt_booking(start, end, focus_length):
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
  Book time into first delta > g_user.user.focus_length over user's next 7 days.

  """

  g_users = GoogleCalendarUser.query.all()

  for g_user in g_users:
    credentials = Credentials(**get_credentials_dict(g_user))
    if credentials.expired is False and credentials.valid is True: ## other checks here?
      service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
      events = get_upcoming_events(service)
      utc_events = [set_utc_tz(e, g_user) for e in events]
      
      dates = dict.fromkeys(set([e.get('start').date() for e in utc_events]))
      for k,v in dates.items():
        dates[k] = [e for e in utc_events if e.get('start').date() == k]

      book_date = datetime.datetime.utcnow().date()

      for i in range(1,8):
        book_date = book_date + datetime.timedelta(1)
        workday_start =  pytz.utc.localize(datetime.datetime(book_date.year, book_date.month, book_date.day, user.workday_start.hour, user.workday_start.minute))
        workday_start = workday_start.astimezone(pytz.timezone(g_user.primary_timeZone))
        workday_end = pytz.utc.localize(datetime.datetime(book_date.year, book_date.month, book_date.day,user.workday_end.hour, user.workday_end.minute))
        workday_start = workday_end.astimezone(pytz.timezone(g_user.primary_timeZone))
        day_events = sorted(dates[book_date], key= lambda i: i['start'])

        if attempt_booking(workday_start, day_events[0].get('start'), g_user.user.focus_length):
          dates[book_date].append(dict({'focus_booked': 1}))
          continue
          
        for i in range(len(day_events)-1):
          if attempt_booking(day_events[i].get('end'),day_events[i+1].get('start'), g_user.user.focus_length):
            dates[book_date].append(dict({'focus_booked': 1}))
            break
        
        if dates[book_date][-1].get('focused_booked'):
          continue
        else:
          if attempt_booking(day_events[-1].get('end'), workday_end, g_user.user.focus_length):
            dates[book_date].append(dict({'focus_booked': 1}))
            continue

        dates[book_date].append(dict({'focus_booked': 0}))


"""
How to insert a calendar event
"""

start = datetime.datetime(2020, 2, 2, 22, 26).isoformat()
end = start + datetime.timedelta(0, 7200)

event = {
  'summary': 'Focus Time',
  'location': 'Desk',
  'description': 'Uninterrupted time for your most important work.',
  'start': {
    'dateTime': datetime.datetime(2020, 2, 2, 22, 26).isoformat(),
    'timeZone': g_user.primary_timeZone,
  },
  'end': {
    'dateTime': datetime.datetime(2020, 2, 2, 22, 26).isoformat(),
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


def get_credentials_dict(user):
  return {
    'token': user.auth_token,
    'refresh_token': user.refresh_token,
    'token_uri': 'https://oauth2.googleapis.com/token',
    'client_id': GOOGLE_CLIENT_ID,
    'client_secret': GOOGLE_CLIENT_SECRET,
    'scopes': fix_scopes_string(user.scopes)
  }

