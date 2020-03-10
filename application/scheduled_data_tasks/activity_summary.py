import application.applied_science.data_utils as du
import application.applied_science.data_annotation as da
from application.models import User, ActivityReportRow
import datetime as dt
from application.initialize.db_init import db

def update_user_activity_rows_non_workday():
  utcnow = dt.datetime.utcnow()
  users = User.query.filter(User.fully_authenticated == True).all()
  for user in users:
    start_time_utc = du.rounddown_next_5min(dt.datetime.utcnow() - dt.timedelta(days=10))
    end_time_utc = du.rounddown_next_5min(dt.datetime.utcnow() + dt.timedelta(days=10))
    user_activity_df = du.collaboration_activity_data_for_given_period(user, start_time_utc, end_time_utc)
    user_activity_df = user_activity_df.loc[datetime_in_workhours(user, user_activity_df.datetime_utc) == False]
    user_activity_df['is_collaborative_time'] = da.naive_collaborative_time_series(user_activity_df)
    user_activity_df['is_workday_time'] = False

    replace_filter = ActivityReportRow.datetime_utc.in_(user_activity_df.datetime_utc) \
      & (ActivityReportRow.user_id == user.id)
    delete_result = ActivityReportRow.query.filter(replace_filter).delete(synchronize_session=False)
    print(delete_result)
    db.session.commit()
    print('deleted existing activity')
    # I don't know if a bulk update would be better given the form of the data ¯\_(ツ)_/¯ 
    print(f'non-workday activity DF info for {user.email}:')
    user_activity_df.info()
    user_activity_df.to_sql('activity_report_rows', db.engine, index=False, if_exists='append', method='multi')
    print(f'updated non-workday activity for user {user.email}')

def update_user_activity_rows_workday():
  utcnow = dt.datetime.utcnow()
  users = User.query.filter(User.fully_authenticated == True).all()
  for user in users:
    for day in range(-3, 3, 1):

      # assumes user's workday_start > workday_end
      start_time_utc = utcnow.replace(hour=user.workday_start.hour, minute=user.workday_start.minute, \
                                            second=0, microsecond=0) + dt.timedelta(days=day)
      end_time_utc = utcnow.replace(hour=user.workday_end.hour, minute=user.workday_end.minute-5, \
                                            second=0, microsecond=0) + dt.timedelta(days=day)
      if start_time_utc.weekday() in du.MONDAY_TO_FRIDAY:
        user_activity_df = du.collaboration_activity_data_for_given_period(user, start_time_utc, end_time_utc)
        user_activity_df['focused_work_period_start_utc'] = da.focused_work_calculation(user_activity_df, da.gloria_mark, df_size=5)
        user_activity_df['is_refocus_time'] = da.get_refocus_times(user_activity_df).fillna(False)
        user_activity_df['is_focus_time'] = da.get_focus_times(user_activity_df).fillna(False)
        user_activity_df['is_collaborative_time'] = (user_activity_df.is_focus_time == False) \
          & (user_activity_df.is_refocus_time == False)
        user_activity_df['is_workday_time'] = True
        delete_result = ActivityReportRow.query.filter((ActivityReportRow.datetime_utc >= start_time_utc) & (ActivityReportRow.datetime_utc <= end_time_utc) & (ActivityReportRow.user_id == user.id)).delete()
        print(delete_result)
        db.session.commit()
        print('deleted existing activity')
        # I don't know if a bulk update would be better given the form of the data ¯\_(ツ)_/¯ 
        print(f'future workday activity DF info for {user.email}:')
        user_activity_df.info()
        user_activity_df.to_sql('activity_report_rows', db.engine, index=False, if_exists='append', method='multi')
        print(f'updated future workday activity for user {user.email}')
      
def datetime_in_workhours(user, utc_datetime):
  is_workday = (utc_datetime + dt.timedelta(hours=user.timezone_offset_hours)).dt.dayofweek.isin(du.MONDAY_TO_FRIDAY)
  in_user_workday = (utc_datetime.dt.time < user.workday_end.time()) \
      & (utc_datetime.dt.time >= user.workday_start.time())
  return is_workday & in_user_workday
