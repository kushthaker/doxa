from datetime import datetime
from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

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

	def __repr__(self):
		return "User('%s','%s','%s')" % (self.username, self.email, self.image_file)

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
	first_name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)
	slack_username = db.Column(db.String(100), nullable=False)
	is_authenticated = db.Column(db.Boolean, nullable=False, default=False)
	authentication_oauth_access_token = db.Column(db.String(200))
	is_deleted_on_slack = db.Column(db.Boolean, nullable=False, default=False)
	created_date = db.Column(db.DateTime, nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	slack_timezone_label = db.Column(db.String(100))
	slack_timezone_offset = db.Column(db.Integer)

	def __repr__(self):
			return 'SlackUser(%s, %s, %s)' % (self.first_name + self.last_name, self.id, self.slack_user_api_id)

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

class RawSlackEvent(db.Model, EnhancedDBModel):
	__tablename__ = 'raw_slack_events'
	id = db.Column(db.Integer, primary_key=True)
	json_data = db.Column(db.JSON(none_as_null=True), nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
	# slack_team_id = db.Column(db.String(100), nullable=False)
	# need a team ID in here, so we can query 

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
