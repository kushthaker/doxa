from numpy.lib.stride_tricks import as_strided as stride
import datetime as dt
import pandas as pd
from application.models import GoogleCalendarEvent, SlackUserEvent, SlackConversationRead
import numpy as np
from sqlalchemy import any_
import math

def roll(df, w, **kwargs):
  # returns iterable of DataFrames each having some length (for window-type functions)
  v = df.values
  d0, d1 = v.shape
  s0, s1 = v.strides

  a = stride(v, (d0 - (w - 1), w, d1), (s0, s0, s1))

  rolled_df = pd.concat({
      row: pd.DataFrame(values, columns=df.columns)
      for row, values in zip(df.index, a)
  })
  return rolled_df.groupby(level=0, **kwargs)

def convert_to_user_timezone_function(slack_timezone_offset):
  return lambda datetime: datetime + dt.timedelta(hours=slack_timezone_offset / 3600.0)

# this is functional programming: it returns a callable function
def convert_to_utc_timezone_function(slack_timezone_offset):
  return lambda datetime: datetime - dt.timedelta(hours=slack_timezone_offset / 3600.0)

def build_google_calendar_event_date_filter(start_utc_datetime, end_utc_datetime):
  start_between_filter = (GoogleCalendarEvent.start_time >= start_utc_datetime) \
    & (GoogleCalendarEvent.start_time < end_utc_datetime)
  end_between_filter = (GoogleCalendarEvent.end_time >= start_utc_datetime) \
    & (GoogleCalendarEvent.end_time < end_utc_datetime)
  encompass_filter = (GoogleCalendarEvent.start_time < start_utc_datetime) \
    & (GoogleCalendarEvent.end_time > end_utc_datetime)
  return start_between_filter | end_between_filter | encompass_filter

def build_slack_user_event_date_filter(start_utc_datetime, end_utc_datetime):
  return (SlackUserEvent.event_datetime >= start_utc_datetime) & (SlackUserEvent.event_datetime < end_utc_datetime) \
    & (SlackUserEvent.slack_event_type == any_(['message', 'reaction_added', 'reaction_removed']))

def build_slack_conversation_read_date_filter(start_utc_datetime, end_utc_datetime):
  return (SlackConversationRead.period_start_datetime >= start_utc_datetime) \
    & (SlackConversationRead.period_start_datetime < end_utc_datetime)

def create_pandas_datetime_series(start, end, frequency='5T'):
  '''
    start: the desired start time of the timeseries
    end: the desired end time of the time series
    frequency: optional, the frequency at which time indices occur in the series (default is '5T', or five minutes)
  '''
  return pd.date_range(start=start,end=end, freq=frequency)

def rounddown_next_5min(event_datetime):
  event_datetime = pd.Timestamp(event_datetime)
  nsecs = event_datetime.minute*60 + event_datetime.second + event_datetime.microsecond*1e-6
  delta = -math.floor(nsecs / 300) * 300 + nsecs
  return event_datetime - dt.timedelta(seconds=delta)

vector_rounddown_next_5min = np.vectorize(rounddown_next_5min, otypes=[dt.datetime]) # allows this function to be called on dataframe column

str_index_fnc = lambda real_datetime: str(real_datetime)
str_index_fnc_vec = np.vectorize(str_index_fnc)

def add_time_delta_to_time(time, delta):
  new_datetime = dt.date(1996, 2, 7)
  return (dt.datetime.combine(new_datetime, time) + delta).time()

def workday_time_filter(df, local_start_time=(8, 30), local_end_time=(17, 30), hour_timezone_offset=-5):
  '''
    df: activity dataframe with datetime index
    local_start_time: user's hours / minutes for their day start, in a tuple
    local_start_time: user's hours / minutes for their day end, in a tuple
    hour_timezone_offset: user's timezone offset from UTC, in hours. Defaults to -5: (ET)
  '''
  start_time_utc = add_time_delta_to_time(dt.time(*local_start_time), dt.timedelta(hours=hour_timezone_offset))
  end_time_utc = add_time_delta_to_time(dt.time(*local_end_time), dt.timedelta(hours=hour_timezone_offset))
  return df.loc[(df.index.time >= start_time_utc) & (df.index.time < end_time_utc)]

def workday_weekend_filter(df, weekend_days=(5, 6), hour_timezone_offset=-5):
  '''
    df: activity dataframe with datetime index
    weekend_days: tuple or list with day numbers corresponding to weekend days. Defaults to (5, 6) (Saturday / Sunday)
    hour_timezone_offset: user's timezone offset from UTC, in hours. Defaults to -5: (ET)
  '''
  weekend_days = set(weekend_days)
  return df.loc[(df.index + dt.timedelta(hours=hour_timezone_offset)).weekday.isin(weekend_days) == False]

def is_collaborative_naive(df, min_interrupt_len=1):
  '''
    df: a short period pandas Dataframe which can be looked at to determine
      whether this period contains collaborative time.
    min_interrupt_len: the minimum interrupt length required to determine
      whether an interruption to focused work time
  '''
  read_interruptions = df[SLACK_CONVERSATION_READ_COLUMN_NAME] >= 1
  user_event_interruptions = df[SLACK_USER_EVENT_COLUMN_NAME] >= 1
  if len(df.loc[read_interruptions | user_event_interruptions]) >= 1:
    return True
  return len(df.loc[read_interruptions | user_event_interruptions] >= 1)

def slack_user_event_data(user, start_datetime_utc, end_datetime_utc):
  '''
    user: a User model, from which data will be queried
    start_datetime_utc: the start datetime where data will be queried from, in UTC
    end_datetime_utc: the end datetime where data will be queried from, in UTC
    ----
    returns a raw pandas Dataframe of the SlackUserEvent model which falls in the given timeframe
  '''
  slack_user_event_filter = (SlackUserEvent.slack_user_id == user.slack_user.id) & \
  build_slack_user_event_date_filter(start_datetime_utc, end_datetime_utc)
  slack_user_event_df = pd.read_sql(SlackUserEvent.query.filter(\
                          slack_user_event_filter).statement, SlackUserEvent.query.session.bind)
  return slack_user_event_df
  
def slack_conversation_read_data(user, start_datetime_utc, end_datetime_utc):
  '''
    user: a User model, from which data will be queried
    start_datetime_utc: the start datetime where data will be queried from, in UTC
    end_datetime_utc: the end datetime where data will be queried from, in UTC
    ----
    returns a raw pandas Dataframe of the SlackConversationRead model which falls in the given timeframe
  '''
  slack_conversation_read_filter = \
    (SlackConversationRead.slack_user_id == user.slack_user.id) \
    & build_slack_conversation_read_date_filter(start_datetime_utc, end_datetime_utc)
  slack_conversation_read_df = pd.read_sql(SlackConversationRead.query.filter(slack_conversation_read_filter) \
                                           .statement, SlackConversationRead.query.session.bind)
  return slack_conversation_read_df


def google_calendar_event_data(user, start_datetime_utc, end_datetime_utc, df=False):
  '''
    user: User model object, from which data will be queried
    start_datetime_utc: the start datetime.datetime where data will be queried from, in UTC
    end_datetime_utc: the end datetime.datetime where data will be queried from, in UTC
    df: boolean
    ----
    returns a raw pandas Dataframe of the SlackConversationRead model which falls in the given timeframe (if `df` is 
    set to True), otherwise returns a list of GoogleCalendarEvent objects
  '''
  google_calendar_event_filter = (GoogleCalendarEvent.google_calendar_user_id == \
                                    user.google_calendar_user.id) \
                                    & build_google_calendar_event_date_filter(start_datetime_utc, end_datetime_utc)
  if df:
    google_calendar_event_df = pd.read_sql(GoogleCalendarEvent.query.filter \
                                (google_calendar_event_filter).statement, GoogleCalendarEvent.query.session.bind)
    return google_calendar_event_df
  google_calendar_events = GoogleCalendarEvent.query.filter(google_calendar_event_filter).all()
  return google_calendar_events

def is_collaborative_meeting(google_calendar_event):
  '''
    This can be used to check whether the meeting is considered "collaborative" - AKA has multiple attendees, is during work hours, etc.
  '''
  return True

def collaboration_activity_data_for_given_period(user, start_datetime_utc, end_datetime_utc):
  '''
    user: User model object, from which data will be queried
    start_datetime_utc: the start datetime.datetime where data will be queried from, in UTC
    end_datetime_utc: the end datetime.datetime where data will be queried from, in UTC
    df: boolean
    ----
    returns a pandas Dataframe of the user's activity with the following columns:
    documentation TODO
  '''  
  slack_user_event_df = slack_user_event_data(user, start_datetime_utc, end_datetime_utc)
  slack_conversation_read_df = slack_conversation_read_data(user, start_datetime_utc, end_datetime_utc)
  google_calendar_events = google_calendar_event_data(user, start_datetime_utc, end_datetime_utc)

  slack_conversation_read_df['rounded_period_start_datetime'] = \
    vector_rounddown_next_5min(slack_conversation_read_df['period_start_datetime'])
  slack_conversation_read_series = slack_conversation_read_df.groupby( \
                                  by=['rounded_period_start_datetime']).count()['id']
  
  slack_user_event_df['rounded_event_datetime'] = vector_rounddown_next_5min(slack_user_event_df['event_datetime'])
  slack_user_event_series = slack_user_event_df.groupby(by=['rounded_event_datetime']).count()['id']

  datetime_index = pd.DatetimeIndex(pd.date_range(start=rounddown_next_5min(start_datetime_utc), \
                                                  end=rounddown_next_5min(end_datetime_utc), freq='5T'))
  activity_df = pd.DataFrame(datetime_index, index=datetime_index, columns=['datetime_utc'])
  
  activity_df['slack_conversation_read_count'] = slack_conversation_read_series
  activity_df['slack_conversation_read_count'] = activity_df['slack_conversation_read_count'].fillna(0)
  
  activity_df['slack_user_event_count'] = slack_user_event_series
  activity_df['slack_user_event_count'] = activity_df['slack_user_event_count'].fillna(0)
  
  activity_df['google_calendar_event_id'] = np.nan
  activity_df['google_calendar_event_count'] = 0
  for calendar_event in google_calendar_events:
    if is_collaborative_meeting(calendar_event):
      activity_df.loc[(activity_df.index >= calendar_event.start_time) \
                      & (activity_df.index < calendar_event.end_time), \
                      ['google_calendar_event_id']] = calendar_event.id
      activity_df.loc[(activity_df.index >= calendar_event.start_time) \
                      & (activity_df.index < calendar_event.end_time), \
                      ['google_calendar_event_count']] += 1
  activity_df.name = f'Collaboration data for User {user.id} from f{start_datetime_utc} to f{end_datetime_utc}'
  activity_df['user_id'] = user.id
  return activity_df

def deepwork_streak_calculation(df, collab_func=None, streak_length=3, interruption_period_length=2):
  '''
    df: pandas Dataframe with datetime index. The index should have
      periods which have an even separation (standard is five minutes)
    streak_length: the minimum number of periods without collaborative time determining whether focused work has begun
    collab_func: the function which gets passed a set of periods to determine whether collaborative time has occurred
    interruption_period_length: the number of periods required for a period of focused work time to be considered 
    "interrupted".
    A streak is assumed to occur if collaborative time has not occurred for the minimum streak length
  '''

  # periods are 5 minutes each
  REQ_STREAK_LENGTH_PERIODS = streak_length
  INTERRUPTION_PERIOD_LENGTH = interruption_period_length
  PERIOD_LENGTH = dt.timedelta(minutes=5)
  
  # keeping track of state across looks
  streak = pd.Series(index=df.index) # needs to be pandas._libs.tslibs.timestamps.Timestamp series
  dumb = pd.Series([1, 2, 3])
  streak_start = None
  in_streak = False
  final_period = df.index[-1]
  def get_streak(mini_df):
    nonlocal streak, streak_start, in_streak, final_period
    interrupt_index = mini_df.index[-INTERRUPTION_PERIOD_LENGTH:]
    final_index = mini_df.index[-1][0] + PERIOD_LENGTH*(REQ_STREAK_LENGTH_PERIODS - 1)
    
    if collab_func(mini_df.loc[interrupt_index], min_interrupt_len=INTERRUPTION_PERIOD_LENGTH):
      if in_streak:
        streak[final_index] = streak_start
        in_streak = False
        streak_start = None
    else:
      if not in_streak:
        # checking fully uninterrupted time
        if not collab_func(mini_df, min_interrupt_len=INTERRUPTION_PERIOD_LENGTH):
          in_streak = True
          streak_start = mini_df.index[0][0]
      if (final_index == final_period) & in_streak:
        streak[final_period] = streak_start
    
  roll(df, REQ_STREAK_LENGTH_PERIODS).apply(get_streak)
  return streak

# can likely change these arguments to kwargs later to make this stuff more generalizable
def is_collaborative_time(df, min_interrupt_len=None, \
  min_interrupt_read_amount=1, min_interrupt_send_amount=1):
  '''
    df: a short period pandas Dataframe which can be looked at to determine whether
      this period contains collaborative time.
    min_interrupt_len: the minimum interrupt length required to determine
      whether an interruption to focused work time
    min_interrupt_read_amount: the minimum number of reads which must occur in a period to determine
      whether message reads make the period "collaborative"
    min_interrupt_send_amount: the minimum number of sends which must occur in a period to determine
      whether message sends make the period "collaborative"
  '''
  if not min_interrupt_len:
    min_interrupt_len = len(df)
  read_interruptions = df[SLACK_CONVERSATION_READ_COLUMN_NAME] >= min_interrupt_read_amount
  user_event_interruptions = df[SLACK_USER_EVENT_COLUMN_NAME] >= min_interrupt_send_amount
  if len(df.loc[read_interruptions | user_event_interruptions]) >= min_interrupt_len:
    return True
  return False