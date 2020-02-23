import application.applied_science.data_utils as du
from application.models import User, ActivityReportRow
import datetime as dt
from application.initialize.db_init import db

def update_user_activity_data_rows():
  start_time_utc = du.rounddown_next_5min(dt.datetime.now() - dt.timedelta(days=5))
  end_time_utc = du.rounddown_next_5min(dt.datetime.now() + dt.timedelta(days=5))
  users = User.query.filter(User.fully_authenticated == True).all()

  for user in users:
    user_activity_df = du.collaboration_activity_data_for_given_period(user, start_time_utc, end_time_utc)
    delete_result = ActivityReportRow.query.filter((ActivityReportRow.datetime_utc >= start_time_utc) & (ActivityReportRow.datetime_utc <= end_time_utc) & (ActivityReportRow.user_id == user.id)).delete()
    print(delete_result)
    db.session.commit()
    print('deleted existing activity')
    # I don't know if a bulk update would be better given the form of the data ¯\_(ツ)_/¯ 
    print(f'activity DF info for {user.email}:')
    user_activity_df.info()
    
    
    user_activity_df.to_sql('activity_report_rows', db.engine, index=False, if_exists='append', method='multi')
    print('updated activity')