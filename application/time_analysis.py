import os
import flask
from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from flask_login import login_user, current_user, logout_user, login_required
from application.models import (GoogleCalendarEvent, GoogleCalendarUser,User, SlackTeam, SlackUser, RawSlackEvent, 
		SlackConversation, SlackConversationQuery, SlackUserEvent, SlackConversationRead)
import datetime
import pytz
from dateutil import parser
import pandas as pd
import math
import json

"""
Get user's past week events.
Get user's past week reads.
Get user's past week writes.
Calculate collaborative time.
Calculate indepdenent time.

if creator and only participant - focus session.
"""

kush_slack_user_id = 3

def roundup_next_5min(write):
	"""
	from stackoverflow.com/questions/13071384
	"""
	dt = write.event_datetime
	nsecs = dt.minute*60 + dt.second + dt.microsecond*1e-6
	delta = math.ceil(nsecs / 300) * 300 - nsecs
	return dt + datetime.timedelta(seconds=delta)

def create_time_series(date):
	start = datetime.datetime.combine(date, datetime.time(0,0))
	end = start + datetime.timedelta(days=1)
	x = pd.date_range(start=start,end=end, freq='5T')
	x_axis = [pt.to_pydatetime() for pt in x.tolist()]
	return dict.fromkeys(x_axis)

def format_read_time(read):
	r = read.period_end_datetime
	return datetime.datetime(r.year, r.month, r.day, r.hour, r.minute)

def get_meeting_times(meeting):
	x = pd.date_range(start=meeting.start_time, end=meeting.end_time, freq='5T')
	times = [pt.to_pydatetime() for pt in x.tolist()]
	return times

@application.route('/calculate-time')
def calculate_time():
	#get user reads, use date as dict key
	reads = SlackConversationRead.query.filter(SlackConversationRead.slack_user_id == 3).all()
	dates = [read.period_start_datetime.date() for read in reads]
	time_data = dict.fromkeys(set(dates))
	clean_reads = list(map(format_read_time, reads))
	
	#get user writes
	slack_events = SlackUserEvent.query.filter(SlackUserEvent.slack_user_id == 3).all()	
	writes = [write for write in slack_events if write.slack_event_type == 'message' or write.slack_event_type == 'reaction_added']
	clean_writes = list(map(roundup_next_5min, writes))

	#get user meetings
	calendar_events = GoogleCalendarEvent.query.filter(GoogleCalendarEvent.google_calendar_user_id == 7).all()
	meetings = [e for e in events if json.loads(e.json_data).get('attendees')]
	clean_meetings = []
	for m in meetings:
		for time in get_meeting_times(meeting):
			clean_meetings.append(time)

	#create 5min freq series
	for k,v in time_data.items():
		time_data[k] = create_time_series(k)
		for x,v in time_data[k].items():
			time_data[k][x] = {'meeting': 0, 'read': 0, 'write': 0}
			time_data[k][x]['read'] = 1 if x in clean_reads else 0
			time_data[k][x]['write'] = 1 if x in clean_writes else 0
			time_data[k][x]['meeting'] = 1 if x in clean_meetings else 0

	return True







