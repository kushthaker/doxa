from datetime import datetime
from application import db
from datetime import datetime

class User(db.Model):
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
	sub_content = db.Column(db.String(100), nullable=True)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

	def __repr__(self):
		return "Post('%s', '%s', '%s')" % (self.title, self.date_posted, self.sub_content)

class RawSlackEvent(db.Model):
	__tablename__ = 'raw_slack_events'
	id = db.Column(db.Integer, primary_key=True)
	json_data = db.Column(db.JSON(none_as_null=True), nullable=False)
	last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
	
	def __init__(self, json_data={}):
		self.json_data = json_data

	def __repr__(self):
		return "RawSlackEvent(%s)" % self.json_data

	def save(self):
		if self.id == None:
			db.session.add(self)
		return db.session.commit()