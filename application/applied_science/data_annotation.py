import pandas as pd
import application.applied_science.data_utils as du
from application.models import ActivityReportRow
import datetime as dt

def labelled_focus_time_df(user, start_datetime=None, end_datetime=None):
  '''
    Core method to deliver reliable, annotated data to users
  '''
  activity_df = get_activity_report_df(user, start_datetime=None, end_datetime=None)
  activity_df.index = activity_df.datetime_utc
 
  activity_df = label_focus_time(activity_df)
  activity_df = apply_work_hours_label(activity_df, hour_timezone_offset)
  activity_df.index += dt.timedelta(hours=hour_timezone_offset)
  activity_df['datetime_local'] = activity_df.index
  return activity_df

def label_focus_time(df):
  df['is_collaborative'] = naive_collaborative_time_series(df)
  df['is_focused'] = df['is_collaborative'] == False
  return df

def apply_work_hours_label(df, hour_timezone_offset):
  weekend_filter = du.workday_weekend_filter(df, hour_timezone_offset=hour_timezone_offset, return_filter=True)
  workday_filter = du.workday_time_filter(df, hour_timezone_offset=hour_timezone_offset, return_filter=True)
  df['not_work_hours'] = ((weekend_filter) & (workday_filter == False)) | (weekend_filter == False)
  return df

def get_activity_report_df(user, start_datetime=None, end_datetime=None):
  start_datetime, end_datetime = (start_datetime, end_datetime) if (start_datetime and end_datetime) else du.current_user_week_limits(user)
  hour_timezone_offset = user.timezone_offset_hours
  date_filter = (ActivityReportRow.datetime_utc >= start_datetime) & (ActivityReportRow.datetime_utc < end_datetime)
  user_filter = ActivityReportRow.user_id == user.id
  df = pd.read_sql(ActivityReportRow.query.filter(date_filter & user_filter) \
                            .order_by(ActivityReportRow.datetime_utc.asc()).statement, \
                            ActivityReportRow.query.session.bind)
  return df

# Naive focused time calculation
NAIVE_STREAK_LENGTH = 1
MINIMUM_INTERRUPTION_LENGTH = 1
MINIMUM_INTERRUPTION_AMOUNT = 1
MINIMUM_INTERRUPTION_SEND_AMOUNT = 1
MINIMUM_INTERRUPTION_READ_AMOUNT = 1

def naive_collaborative_time_series(df):
  return ((df[du.SLACK_CONVERSATION_READ_COLUMN_NAME] >= 1) | (df[du.SLACK_USER_EVENT_COLUMN_NAME] >= 1) | (df[du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME] >= 1))

# can likely change these arguments to kwargs later to make this stuff more generalizable
def is_collaborative_time(df, min_interrupt_len=1, \
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
  read_interruptions = df[du.SLACK_CONVERSATION_READ_COLUMN_NAME] >= min_interrupt_read_amount
  user_event_interruptions = df[du.SLACK_USER_EVENT_COLUMN_NAME] >= min_interrupt_send_amount
  if (len(df.loc[read_interruptions | user_event_interruptions]) >= min_interrupt_len) | \
    (len(df.loc[df[du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME] > 0]) > 0):
    return True
  return False

def sample_collab_func(mini_df, pfr=1, ipl=1, misa=1, mira=1):
  slack_read_col = mini_df[du.SLACK_CONVERSATION_READ_COLUMN_NAME]
  slack_send_col = mini_df[du.SLACK_USER_EVENT_COLUMN_NAME]
  cal_event_count_col = mini_df[du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME]
  interruptions = mini_df.head(ipl).loc[
    (slack_read_col.head(ipl) > mira)
    | (slack_send_col.head(ipl) > misa) | (cal_event_count_col.head(ipl) > 0)
  ]
  interruption_dt = next(iter(interruptions.datetime_utc), None)

  if(len(mini_df.head(pfr).loc[
    (slack_read_col.head(pfr) > mira)
    | (slack_send_col.head(pfr) > misa)
    | (cal_event_count_col.head(pfr) > 0)]) == 0):
    refocus_dt = mini_df.head(pfr).datetime_utc[-1]
  else:
    refocus_dt = None
  return interruption_dt, refocus_dt

# applied like activity_df['focused_work_period_start'] = da.focused_work_calculation(activity_df, gloria_mark, df_size=5)

def focused_work_calculation(df, collab_func=None, df_size=None, **kwargs):  
  # keeping track of state across looks
  streak = pd.Series(index=df.index) # needs to be pandas._libs.tslibs.timestamps.Timestamp series
  streak_start = None
  in_streak = False
  if not df_size:
    df_size = max(kwargs.values())
  
  def get_streak(mini_df):
    nonlocal streak, streak_start, kwargs
    
    interrupt_time, refocus = collab_func(mini_df, **kwargs)
  # no streak, not interrupted
    if (not streak_start) & (refocus is not None):
      streak_start = refocus
    # streak, interrupted
    elif (streak_start is not None) & (interrupt_time is not None):
      streak[interrupt_time] = streak_start
      streak_start = None
    # last iteration
    elif (mini_df.datetime_utc[-1] == df.datetime_utc[-1]) \
      & (streak_start is not None) & (refocus is not None):
      streak[mini_df.datetime_utc[-1]] = streak_start
    
  du.roll(df, df_size).apply(get_streak)
  return pd.to_datetime(streak)

def gloria_mark(mini_df, pfr=5, ipl=2, mira=2, misa=1):
  # refocus is 5 periods (25 minutes)
  # interruption period is 2 (need to get interrupted 10 minutes in a row)
  # slack interruption is reading 2 messages or sending 1 message
  slack_read_col = mini_df[du.SLACK_CONVERSATION_READ_COLUMN_NAME]
  slack_send_col = mini_df[du.SLACK_USER_EVENT_COLUMN_NAME]
  cal_event_count_col = mini_df[du.GOOGLE_CALENDAR_EVENT_COUNT_COLUMN_NAME]
  interruptions = mini_df.head(ipl).loc[
    (slack_read_col.head(ipl) >= mira)
    | (slack_send_col.head(ipl) >= misa)
  ]
  
  if (len(interruptions) >= ipl) or (cal_event_count_col[0] > 0):
    interruption_dt = mini_df.head(1).datetime_utc[0]
  else:
    interruption_dt = None
  
  if(len(mini_df.head(pfr).loc[
    (slack_read_col.head(pfr) > mira)
    | (slack_send_col.head(pfr) > misa)
    | (cal_event_count_col.head(pfr) > 0)]) == 0):
    refocus_dt = mini_df.head(pfr).datetime_utc[-1]
  else:
    refocus_dt = None
  return interruption_dt, refocus_dt
