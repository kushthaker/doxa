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

def book_upcoming_week_focus_time():
  """
  Book time each day in upcoming week given user preferences.
  """
  g_user = GoogleCalendarUser.query.filter(GoogleCalendarUser.id == 7).first()


d = pytz.UTC.localize(now) 
est = pytz.timeZone(user.primary_timeZone)
a = d.astimezone(est)
a.replace(second=0, microsecond=0)

datetime.timedelta(minutes=60)
datetime.timedelta(minutes=90)
datetime.timedelta(minutes=120)
datetime.timedelta(minutes=150)

a.isoformat()

"""
for event in date
  order by start time
  start workday start <- possible start
  delta = focus_length
  start time first event <- possible end 
  if workday start >= delta, book
    if start of next in start-end first
      use next end
  else set possible end as possible start
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