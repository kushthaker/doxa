from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
	PASSWORDS_MATCH_ERROR = "Passwords must be the same."
	username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', PASSWORDS_MATCH_ERROR)])
	submit = SubmitField('Create Account')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username in use. Please try another.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email in use. Please try another.')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')	
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username in use. Please try another.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email in use. Please try another.')

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Post')

class ChangePasswordForm(FlaskForm):
	PASSWORDS_MATCH_ERROR = 'New passwords must be the same'
	new_password = PasswordField('New Password', validators=[DataRequired()])
	confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password', PASSWORDS_MATCH_ERROR)])

class SlackAuthorizationForm(FlaskForm):
	code = TextAreaField('Slack Authorization Code', validators=[DataRequired()])
