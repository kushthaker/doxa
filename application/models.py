from datetime import datetime
from application.initialize.login_manager_init import login_manager
from application.initialize.db_init import db
from flask_login import UserMixin
from datetime import datetime
import slack
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Index

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
	workday_start = db.Column(db.DateTime, default=datetime(2020, 1, 1, 14, 30))
	workday_end = db.Column(db.DateTime, default=datetime(2020, 1, 1, 22, 30))
	focus_length = db.Column(db.Integer, default=2)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
	posts = db.relationship('Post', backref='author', lazy=True)
	google_calendar_user = db.relationship('GoogleCalendarUser', backref='user', uselist=False)
	slack_user = db.relationship('SlackUser', backref='user', uselist=False)
	github_user = db.relationship('GitHubUser', backref='user', uselist=False)

	def __repr__(self):
		return "User('%s','%s','%s')" % (self.username, self.email, self.image_file)

	def to_dict(self):
		return dict(id=self.id, username=self.username, email=self.email)

	def user_details(self):
		return dict(id=self.id, username=self.username, email=self.email, \
					github_user_id=self.github_user.id if self.github_user else None, \
		            google_calendar_user_id=self.google_calendar_user.id if self.google_calendar_user else None, \
		            slack_user_id=self.slack_user.id if self.slack_user else None)
		# GCal user may be null, so we need to account for this. username, email, id are req'd fields
	@hybrid_property
	def fully_authenticated(self):
		return (self.google_calendar_user != None) & (self.slack_user != None)

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

#Stores GitHub user information
class GitHubUser(db.Model, EnhancedDBModel):
	__tablename__ = 'github_users'
	id = db.Column(db.Integer, primary_key=True)
	github_api_user_id = db.Column(db.Integer, nullable=False)
	github_oauth_access_token = db.Column(db.String(200))
	github_email_address = db.Column(db.String(300))
	github_username = db.Column(db.String(100), nullable=True)
	is_authenticated = db.Column(db.Boolean, nullable=False, default=False)
	is_deleted_on_github = db.Column(db.Boolean, nullable=False, default=False)
	created_at = db.Column(db.DateTime, nullable=True)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return 'GitHubUser(%s, %s, %s)' % (self.github_username, self.id, self.user_id)

class GitHubRepo(db.Model, EnhancedDBModel):
	__tablename__ = 'github_repos'
	id = db.Column(db.Integer, primary_key=True)
	github_api_repo_id = db.Column(db.Integer, nullable=False)
	#Repository names can be up to 100 characters long
	#https://github.com/evalEmpire/gitpan/issues/123
	name = db.Column(db.String(100), nullable = False)
	created_at = db.Column(db.DateTime, nullable=True)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=True)
	#GitHub API user id of owner
	github_api_owner_id = db.Column(db.Integer, nullable=True)
	organization = db.Column(db.String(100), nullable=True)
	is_private = db.Column(db.Boolean, nullable=False, default=False)

	def __repr__(self):
		return 'GitHubRepo(%s, %s, %s)' % (self.name, self.id, self.github_api_owner_id)

class GitHubCommit(db.Model, EnhancedDBModel):
	__tablename__ = 'github_commits'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	github_api_repo_id = db.Column(db.Integer, nullable=False)
	#Author is assumed original writer of the code
	#(might be different from committer in cases such as patches or history rewrites)
	github_api_author_id = db.Column(db.Integer, nullable=False)
	github_api_committer_id = db.Column(db.Integer, nullable=True)
	#Full-length GitHub sha are 40 hex characters
	#https://stackoverflow.com/a/18134919
	sha = db.Column(db.String(40), nullable=False)
	github_api_committed_at = db.Column(db.DateTime, nullable=False)
	insertions = db.Column(db.Integer, nullable=True)
	deletions = db.Column(db.Integer, nullable=True)
	edit_points = db.Column(db.Integer, nullable=True)
	files_changed = db.Column(db.Integer, nullable=True)
	impact_score = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return 'GitHubCommit(%s, %s, %s, %s)' % (self.id, self.github_api_repo_id, self.github_api_author_id, self.impact_score)


class GitHubPullRequest(db.Model, EnhancedDBModel):
	__tablename__ = 'github_pull_requests'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	github_api_pr_id = db.Column(db.Integer, nullable=False)
	github_api_repo_id = db.Column(db.Integer, nullable=False)
	github_api_author_id = db.Column(db.Integer, nullable=False)
	base_sha = db.Column(db.String(40), nullable=False)
	head_sha = db.Column(db.String(40), nullable=False)
	github_api_opened_at = db.Column(db.DateTime, nullable=False)
	github_api_closed_at = db.Column(db.DateTime, nullable=True)
	github_api_merged_at = db.Column(db.DateTime, nullable=True)
	insertions = db.Column(db.Integer, nullable=True)
	deletions = db.Column(db.Integer, nullable=True)
	edit_points = db.Column(db.Integer, nullable=True)
	files_changed = db.Column(db.Integer, nullable=True)
	percent_churn = db.Column(db.Float, nullable=True)
	status = db.Column(db.String(10), nullable=True)
	impact_score = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return 'GitHubPullRequest(%s, %s, %s, %s, %s)' % (self.id, self.github_api_pr_id, self.github_api_repo_id, self.github_api_author_id, self.impact_score)

class GitHubIssue(db.Model, EnhancedDBModel):
	__tablename__ = 'github_issues'
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	github_api_issue_id = db.Column(db.Integer, nullable=False)
	github_api_creator_id = db.Column(db.Integer, nullable=False)
	is_open = db.Column(db.Boolean, nullable=True)
	github_api_opened_at = db.Column(db.DateTime, nullable=False)
	github_api_closed_at = db.Column(db.DateTime, nullable=True)
	open_impact_score = db.Column(db.Float, nullable=True)
	closure_impact_score = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return 'GitHubIssue(%s, %s, %s, %s, %s, %s)' % (self.id, self.github_api_issue_id, self.github_api_creator_id, self.open_impact_score, self.closure_impact_score)

class GitHubComment(db.Model, EnhancedDBModel):
	__tablename__ = 'github_comments'
	id = db.Column(db.Integer, primary_key=True)
	github_api_comment_id = db.Column(db.Integer, nullable=False)
	github_api_author_id = db.Column(db.Integer, nullable=False)	
	#Type distinguishes between "commit", "PR", "issue" etc. comments
	#Playing it safe with space allocation
	comment_type = db.Column(db.String(30), primary_key=True)
	#ID of the commit, issue, PR or other that this comment was made on
	github_api_parent_id = db.Column(db.Integer, nullable=False)
	created_at = db.Column(db.DateTime, nullable=False)
	updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, nullable=False)
	github_api_written_at = db.Column(db.DateTime, nullable=False)
	github_api_edited_at = db.Column(db.DateTime, nullable=False)
	impact_score = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return 'GitHubComment(%s, %s, %s, %s, %s, %s)' % (self.id, self.github_api_comment_id, self.github_api_author_id, self.comment_type, self.github_api_parent_id, self.impact_score)

class ActivityReportRow(db.Model):
	__tablename__ = 'activity_report_rows'
	id = db.Column(db.Integer, primary_key=True)
	datetime_utc = db.Column(db.DateTime, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	slack_conversation_read_count = db.Column(db.Integer, nullable=True)
	slack_user_event_count = db.Column(db.Integer, nullable=True)
	google_calendar_event_id = db.Column(db.Integer, db.ForeignKey('google_calendar_events.id'), nullable=True)
	google_calendar_event_count = db.Column(db.Integer, nullable=True)
	__table_args__ = ( \
	                  Index('activity_report_unique_user_datetime', 'user_id', \
	                        'datetime_utc', unique=True),)
	def __repr__(self):
		return f'ActivityReportRow({self.id}, {self.datetime_utc}, {self.user_id})'

