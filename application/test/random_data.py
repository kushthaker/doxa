from application.applied_science import data_utils as du
import datetime as dt
import pandas as pd
import numpy as np

def random_number_of_slack_sends_or_reads(p_no_message=0.5):
  if np.random.uniform() > p_no_message:
    return np.int(np.random.exponential(1.5) + 0.5)
  return 0
  
def random_meeting_id():
  in_meeting = np.random.pareto(2) > 1
  return np.int(np.random.uniform(1000, 5000)) if in_meeting else None

def random_meeting_count(meeting_id=None):
  if meeting_id:
    if np.random.uniform() > 0.96:
      return 2
    return 1
  return 0
  
  
DF_COLUMN_KEY = {
  du.SLACK_CONVERSATION_READ_COLUMN_NAME: random_number_of_slack_sends_or_reads,
  du.SLACK_USER_EVENT_COLUMN_NAME: random_number_of_slack_sends_or_reads,
  du.GOOGLE_CALENDAR_EVENT_ID_COLUMN_NAME: random_meeting_id,
  du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME: random_meeting_count 
}

def date_range(size, interval=dt.timedelta(minutes=5), start=None):
  start = du.rounddown_next_5min(dt.datetime.utcnow()) if (not start) else start
  datetimes = [start]
  next_datetime = start
  for _ in range(size):
    next_datetime = next_datetime + interval
    datetimes.append(next_datetime)
  return datetimes

def insert_streak(length=8):
  vals = []
  for _ in range(length):
    values = {}
    for cn in DF_COLUMN_KEY.keys():
      values[cn] = 0
    values[du.GOOGLE_CALENDAR_EVENT_ID_COLUMN_NAME] = None
    vals.append(values)
  return vals

def generate_sample_data(number_of_periods=50):
  datetime_index = pd.Index(date_range(number_of_periods))
  df_list = []
  for _ in datetime_index:
    if (len(df_list) > 8) & (np.random.uniform() > 0.98):
      df_list[-7:] = insert_streak()
    else:
      values = {}
      for cn in DF_COLUMN_KEY.keys():
        values[cn] = DF_COLUMN_KEY[cn]()
      values[du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME] = DF_COLUMN_KEY[du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME]\
                            (values[du.GOOGLE_CALENDAR_EVENT_ID_COLUMN_NAME])
      df_list.append(values)
  df = pd.DataFrame(df_list, index=datetime_index)
  df['datetime_utc'] = df.index
  return df
