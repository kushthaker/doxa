from datetime import datetime
from application.initialize.login_manager_init import login_manager
from application.initialize.db_init import db
from flask_login import UserMixin
from datetime import datetime
import slack

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ = 'users' # follows general table name paradigm in database (plural)
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
	posts = db.relationship('Post', backref='author', lazy=True)
	google_calendar_user = db.relationship('GoogleCalendarUser', backref='user', uselist=False)
	slack_user = db.relationship('SlackUser', backref='user', uselist=False)

	def __repr__(self):
		return "User('%s','%s','%s')" % (self.username, self.email, self.image_file)

	def to_dict(self):
		return dict(id=self.id, username=self.username, email=self.email)

	def user_details(self):
		return dict(id=self.id, username=self.username, email=self.email, \
		            google_calendar_user_id=self.google_calendar_user.id if self.google_calendar_user else None, \
		            slack_user_id=self.slack_user.id if self.slack_user else None)
		# GCal user may be null, so we need to account for this. username, email, id are req'd fields

class Post(db.Model):
	__tablename__ = 'posts' # follows general table name paradigm in database (plural)
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)

	def __repr__(self):
		return "Post('%s', '%s')" % (self.title, self.date_posted)

	def date_to_string(self):
		return self.date_posted.strftime("%a %b %d %Y %l:%M%p")

class EnhancedDBModel():
	def save(self):
		if self.id == None:
			db.session.add(self)
		return db.session.commit()

	# does not commit session; you have to call db.session.commit() later on
	def update(self, update_dict):
	  model_type = type(self)
	  model_type.query.filter(model_type.id == self.id).update(update_dict)

	# does not commit session
	def delete(self):
		model_type = type(self)
		model_type.query.filter(model_type.id == self.id).delete()

class SlackTeam(db.Model, EnhancedDBModel):
	__tablename__ = 'slack_teams'
	id = db.Column(db.Integer, primary_key=True)
	api_scope = db.Column(db.String(1000), nullable=True)
	slack_team_api_id = db.Column(db.String(100), nullable=False, unique=True)
	slack_team_name = db.Column(db.String(100), nullable=False)
	api_access_token = db.Column(db.String(100), nullable=True)
	authenticated_at = db.Column(db.DateTime, nullable=True)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

	def update_registration(self, new_slack_team):
		if new_slack_team.slack_team_api_id != self.slack_team_api_id:
			raise ValueError("Old slack team ID is not the same as new Slack team ID")
		self.api_scope = new_slack_team.api_scope
		self.slack_team_name = new_slack_team.slack_team_name
		self.api_access_token = new_slack_team.api_access_token
		self.datetime_authenticated = datetime.utcnow()

	def slack_users(self):
		return SlackUser.query.filter(SlackUser.slack_team_id == self.id).all()	

	def slack_conversations(self):
		return SlackConversation.query.filter(SlackConversation.slack_team_id == self.id).all()

	def __repr__(self):
		return "SlackTeam('%s', '%s')" % (self.slack_team_name, self.slack_team_api_id)

	def __init__(self, oauth_response_json):
		self.api_scope = oauth_response_json.get('scope')
		self.slack_team_id = oauth_response_json.get('team_id')
		self.slack_team_api_id = oauth_response_json.get('team_id')
		self.slack_team_name = oauth_response_json.get('team_name')
		self.api_access_token = oauth_response_json.get('access_token')
		self.datetime_authenticated = datetime.utcnow()

class SlackUser(db.Model, EnhancedDBModel):
	__tablename__ = 'slack_users'
	id = db.Column(db.Integer, primary_key=True)
	slack_user_api_id = db.Column(db.String(100), nullable=False)
	slack_team_id = db.Column(db.Integer, db.ForeignKey('slack_teams.id'), nullable=False)
	slack_email_address = db.Column(db.String(300))
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	slack_username = db.Column(db.String(100), nullable=False)
	is_authenticated = db.Column(db.Boolean, nullable=False, default=False)
	authentication_oauth_access_token = db.Column(db.String(200))
	is_deleted_on_slack = db.Column(db.Boolean, nullable=False, default=False)
	created_date = db.Column(db.DateTime, nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	slack_timezone_label = db.Column(db.String(100))
	slack_timezone_offset = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def slack_team(self):
		return SlackTeam.query.filter(SlackTeam.id == self.slack_team_id).one()

	def __repr__(self):
			return 'SlackUser(%s, %s, %s)' % (self.first_name + self.last_name, self.id, self.slack_user_api_id)

	def slack_client(self):
		if self.is_authenticated:
			return slack.WebClient(self.authentication_oauth_access_token)
		else:
			return None

class SlackConversation(db.Model, EnhancedDBModel):
	__tablename__ = 'slack_conversations'
	id = db.Column(db.Integer, primary_key=True)
	slack_conversation_api_id = db.Column(db.String(100), nullable=False)
	slack_team_id = db.Column(db.Integer, db.ForeignKey('slack_teams.id'), nullable=False)
	conversation_type = db.Column(db.String(100), nullable=False) # 'im', 'mpim', 'channel', 'private_channel'
	conversation_name = db.Column(db.String(100)) # can be null for IM conversation
	is_deleted = db.Column(db.Boolean, nullable=False, default=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)

class SlackConversationQueryRun(db.Model, EnhancedDBModel):
	__tablename__ = 'slack_conversation_query_runs'
	id = db.Column(db.Integer, primary_key=True)
	query_start_time = db.Column(db.DateTime, nullable=False)
	query_end_time = db.Column(db.DateTime)
	slack_user_id = db.Column(db.Integer, db.ForeignKey('slack_users.id'), nullable=False)

class SlackConversationQuery(db.Model):
  __tablename__ = 'slack_conversation_queries'
  id = db.Column(db.Integer, primary_key=True)
  slack_user_id = db.Column(db.Integer, db.ForeignKey('slack_users.id'), nullable=False)
  slack_conversation_id = db.Column(db.Integer, db.ForeignKey('slack_conversations.id'), nullable=False)
  query_datetime = db.Column(db.DateTime, nullable=False)
  last_read_datetime = db.Column(db.DateTime, nullable=False)
  last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
  slack_conversation_query_run_id = db.Column(db.Integer, db.ForeignKey('slack_conversation_query_runs.id'), nullable=False)

class SlackUserEvent(db.Model, EnhancedDBModel):
	__tablename__ = 'slack_user_events'
	id = db.Column(db.Integer, primary_key=True)
	slack_user_id = db.Column(db.Integer, db.ForeignKey('slack_users.id'), nullable=False)
	raw_slack_event_id = db.Column(db.Integer, db.ForeignKey('raw_slack_events.id')) # may be null if polled from Slack API
	slack_event_api_id = db.Column(db.String(100), nullable=False)
	event_datetime = db.Column(db.DateTime, nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	slack_event_type = db.Column(db.String(100), nullable=False)
	slack_event_subtype = db.Column(db.String(100))

	def __repr__(self):
		return "SlackUserEvent(id: %s, slack_user_id: %s, slack_event_api_id: %s, slack_event_type: %s, slack_event_subtype: %s)" % \
			(self.id, self.slack_user_id, self.slack_event_api_id, self.slack_event_type, self.slack_event_subtype or '')

class SlackConversationRead(db.Model):
	__tablename__ = 'slack_conversation_reads'
	id = db.Column(db.Integer, primary_key=True)
	slack_conversation_query_id = db.Column(db.Integer, db.ForeignKey('slack_conversation_queries.id'), nullable=False, unique=True)
	slack_user_id = db.Column(db.Integer, db.ForeignKey('slack_users.id'), nullable=False)
	slack_conversation_id = db.Column(db.Integer, db.ForeignKey('slack_conversations.id'), nullable=False)
	period_start_datetime = db.Column(db.DateTime, nullable=False)
	period_end_datetime = db.Column(db.DateTime, nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)

class RawSlackEvent(db.Model, EnhancedDBModel):
	__tablename__ = 'raw_slack_events'
	id = db.Column(db.Integer, primary_key=True)
	json_data = db.Column(db.JSON(none_as_null=True), nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

	def __init__(self, json_data={}):
		self.json_data = json_data

	def __repr__(self):
		return "RawSlackEvent(%s)" % self.json_data

class APSchedulerJob(db.Model):
	__tablename__ = 'apscheduler_jobs'
	id = db.Column(db.Integer, primary_key=True)
	next_run_time = db.Column(db.Float, nullable=True, index=True)
	job_state = db.Column(db.LargeBinary, nullable=False)
	# created this after I realized that a migration will be made to delete it

class GoogleCalendarUser(db.Model, EnhancedDBModel):
	__tablename__ = 'google_calendar_users'
	id = db.Column(db.Integer, primary_key=True)
	google_email = db.Column(db.String(300), nullable=False)
	auth_token = db.Column(db.String(300), nullable=False)
	refresh_token = db.Column(db.String(300))
	scopes = db.Column(db.String(300), nullable=False)
	primary_timeZone = db.Column(db.String(300), nullable=False)
	primary_etag = db.Column(db.String(300), nullable=False)
	primary_color_id = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	google_calendar_events = db.relationship('GoogleCalendarEvent', backref='google_calendar_user', lazy=True)

	def __repr__(self):
		return "GoogleCalendarUser('%s','%s','%s')" % (self.google_email, self.primary_timeZone, self.created_at)

class GoogleCalendarEvent(db.Model, EnhancedDBModel):
	__tablename__ = 'google_calendar_events'
	id = db.Column(db.Integer, primary_key=True)
	google_id = db.Column(db.String(200), nullable=False)
	ical_uid = db.Column(db.String(200), nullable=False)
	start_time = db.Column(db.DateTime, nullable=False)
	end_time = db.Column(db.DateTime, nullable=False)
	summary = db.Column(db.String(300), nullable=False)
	description = db.Column(db.Text)
	organizer_email = db.Column(db.String(200), nullable=False)
	organizer_self = db.Column(db.Boolean, default=False)
	json_data = db.Column(db.JSON)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
	google_calendar_user_id = db.Column(db.Integer, db.ForeignKey('google_calendar_users.id'))

	def __repr__(self):
		return "GoogleCalendarEvent('%s','%s','%s','%s')" % (self.organizer_email, self.start_time, self.end_time, self.google_calendar_user_id)
