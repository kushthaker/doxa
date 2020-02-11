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
  g_user = GoogleCalendarUser.query.all()
  
  for user in users:
    credentials = Credentials(**get_credentials_dict(user))
    if credentials.expired is False and credentials.valid is True:
      service = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

d = pytz.UTC.localize(now) 
est = pytz.timeZone(user.primary_timeZone)
a = d.astimezone(est)
a.replace(second=0, microsecond=0)

datetime.timedelta(minutes=60)
datetime.timedelta(minutes=90)
datetime.timedelta(minutes=120)
datetime.timedelta(minutes=150)

a.isoformat()

  now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
  events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=20, singleEvents=True, orderBy='startTime').execute()
  events = events_result.get('items', [])

workday_start = datetime.datetime(2020, 2, 11, 14, 30, 00)
workday_end = datetime.datetime(2020, 2, 11, 14, 30, 00)

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

def utc_datetimes(event):
  if event.get('start').get('dateTime'):
    s_dt = parser.parse(event.get('start').get('dateTime')).replace(tzinfo=pytz.UTC)
    e_dt = parser.parse(event.get('end').get('dateTime')).replace(tzinfo=pytz.UTC)
  elif event.get('start').get('date'):
    s_dt = parser.parse(event.get('start').get('date')).replace(tzinfo=pytz.UTC)
    e_dt = parser.parse(event.get('end').get('date')).replace(tzinfo=pytz.UTC)
  event_id = event.get('id')
  return dict({'start':st,'end':et,'event_id':event_id})

p_events = [utc_datetimes(e) for e in events]

for e in p_events:
  workday_start = datetime.datetime(e.get('start').date().year, e.get('start').date().month, e.get('start').date().day, user.workday_start.hour, user.workday_start.minute)
  workday_end = datetime.datetime(e.get('start').date().year, e.get('start').date().month, e.get('start').date().day, user.workday_end.hour, user.workday_end.minute)

  if (e.get('start').hour == 0 and e.get('start').minute == 0) and (e.get('end').hour == 0 and e.get('end').minute == 0):
    """all day event"""
  else:

for k,v in dates.items():
  dates[k] = [e for e in p_events if e.get('start').date() == k]
  dates[k].append(dict({'workday_start': datetime.datetime(k.year, k.month, k.day, user.workday_start.hour, user.workday_start.minute)}))
  dates[k].append(dict({'workday_end': datetime.datetime(k.year, k.month, k.day,user.workday_end.hour, user.workday_end.minute)}))
  dates[k].append(dict({'focus_booked': 0}))





def get_free_times(events):
  st = parser.parse(event.get('start').get('dateTime')).replace(tzinfo=pytz.UTC)
  et = parser.parse(event.get('end').get('dateTime')).replace(tzinfo=pytz.UTC)
  event_id = event.get('id')

  free_times = []
  m_interrupts = []

  for event in events:
    st = parser.parse(event.get('start').get('dateTime')).replace(tzinfo=pytz.UTC)
    et = parser.parse(event.get('end').get('dateTime')).replace(tzinfo=pytz.UTC)
    event_id = event.get('id')
    meetings.append({'start':st,'end':et,'event_id':event_id})

  free_start = datetime.datetime(m_interrupts[0].get('start').year, m_interrupts[0].get('start').month, m_interrupts[0].get('start').day, 8, 00, 00, tzinfo=pytz.UTC)
  free_end = datetime.datetime(m_interrupts[0].get('end').year, m_interrupts[0].get('end').month, m_interrupts[0].get('end').day, 18, 00, 00, tzinfo=pytz.UTC)
  for i in range(len(m_interrupts)-1):
    start_block = {'start':free_start,'end':m_interrupts[i].get('start')}
    if free_start.date() == m_interrupts[i+1].get('start').date():
      free_times.append(start_block)
      free_times.append({'start':m_interrupts[i].get('end'),'end':m_interrupts[i+1].get('start')})
      free_times.append({'start':m_interrupts[i+1].get('end'),'end':free_end})
    else:
      free_times.append(start_block)
      free_times.append({'start':m_interrupts[i].get('end'),'end':free_end})
      free_start = datetime.datetime(m_interrupts[i+1].get('start').year, m_interrupts[i+1].get('start').month, m_interrupts[i+1].get('start').day, 8, 00, 00, tzinfo=pytz.UTC)
      free_end = datetime.datetime(m_interrupts[i+1].get('end').year, m_interrupts[i+1].get('end').month, m_interrupts[i+1].get('end').day, 18, 00, 00, tzinfo=pytz.UTC)

  for time in free_times:
    print(time.get('start').strftime("%c"))
    print(time.get('end').strftime("%c"))
    print("\n")


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
  now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
  events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=20, singleEvents=True, orderBy='startTime').execute()
  events = events_result.get('items', [])

  if not events:
    print('No upcoming events found.')

  return events

def get_credentials_dict(user):
  return {
    'token': user.auth_token,
    'refresh_token': user.refresh_token,
    'token_uri': 'https://oauth2.googleapis.com/token',
    'client_id': GOOGLE_CLIENT_ID,
    'client_secret': GOOGLE_CLIENT_SECRET,
    'scopes': fix_scopes_string(user.scopes)
  }

