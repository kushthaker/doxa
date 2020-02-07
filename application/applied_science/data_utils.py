from numpy.lib.stride_tricks import as_strided as stride
import datetime as dt
import pandas as pd
from application.models import GoogleCalendarEvent, SlackUserEvent, SlackConversationRead
import numpy as np
# returns iterable of DataFrames each having some length (for window type functions)
def roll(df, w, **kwargs):
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
  start_between_filter = (GoogleCalendarEvent.start_time >= start_utc_datetime) & (GoogleCalendarEvent.start_time < end_utc_datetime)
  end_between_filter = (GoogleCalendarEvent.end_time >= start_utc_datetime) & (GoogleCalendarEvent.end_time < end_utc_datetime)
  encompass_filter = (GoogleCalendarEvent.start_time < start_utc_datetime) & (GoogleCalendarEvent.end_time > end_utc_datetime)
  return start_between_filter | end_between_filter | encompass_filter

def build_slack_user_event_date_filter(start_utc_datetime, end_utc_datetime):
  return (SlackUserEvent.event_datetime >= start_utc_datetime) & (SlackUserEvent.event_datetime < end_utc_datetime) \
    & (SlackUserEvent.slack_event_type == any_(['message', 'reaction_added', 'reaction_removed']))

def build_slack_conversation_read_date_filter(start_utc_datetime, end_utc_datetime):
  return (SlackConversationRead.period_start_datetime >= start_utc_datetime) & (SlackConversationRead.period_start_datetime < end_utc_datetime)

def create_pandas_datetime_series(start, end):
  return pd.date_range(start=start,end=end, freq='5T')

def rounddown_next_5min(event_datetime):
  event_datetime = pd.Timestamp(event_datetime)
  nsecs = event_datetime.minute*60 + event_datetime.second + event_datetime.microsecond*1e-6
  delta = -math.floor(nsecs / 300) * 300 + nsecs
  return event_datetime - dt.timedelta(seconds=delta)

vector_rounddown_next_5min = np.vectorize(rounddown_next_5min) # allows this function to be called on dataframe column

str_index_fnc = lambda real_datetime: str(real_datetime)
str_index_fnc_vec = np.vectorize(str_index_fnc)

