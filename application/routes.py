import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from application import application, db, bcrypt
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
from application.models import User, Post, RawSlackEvent
from flask_login import login_user, current_user, logout_user, login_required
from application import slack_auth

@application.route('/slack-event', methods=['POST'])
def slack_event():
	print(request)
	try:
		if request.json.get('type') != 'url_verification':
			print(request.json) # this is where we log / store things
			raw_slack_event = RawSlackEvent(json_data = request.json)
			raw_slack_event.save()
			return '200'
		else:
			print(request.json)
			return request.json.get('challenge')
	except:
		print('excepted:')
		print(request.json)
		return '200'
	return '200'

@application.route('/test-db-route', methods=['GET'])
def test_db_route():
	return str(Post.query.all()) # test method to see if application can hit DB in production

posts = [
	{
		'author':'kt',
		'title':'post 1',
		'content':'content 1',
		'date_posted':'April 5 2019'
	},
	{
		'author':'pt',
		'title':'post 2',
		'content':'content 2',
		'date_posted':'April 3 2019'
	},
	{
		'author':'hf',
		'title':'post 3',
		'content':'content 3',
		'date_posted':'April 9 2019'
	}
]

@application.route("/")
def home():         
    return render_template('home.html', posts=posts)

@application.route("/about")
def about():
	return render_template('about.html', title="About")

@application.route("/register", methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Account created for %s!' % form.username.data, 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@application.route("/login", methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Check email and password.', 'danger')
	return render_template('login.html', title='Login', form=form)

@application.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

def save_image(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(application.root_path, 'static/profile_pics', picture_fn)
	form_picture.save(picture_path)
	return picture_fn

@application.route("/account", methods=['GET','POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_image(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Account Updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email

	if current_user.image_file == 'default.jpg':
		image_path = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/07-User-Account-Profile-Pic/flaskblog/static/profile_pics/default.jpg'
	else:
		image_path = '../static/profile_pics/' + current_user.image_file

	return render_template('account.html', title='Account', image_path=image_path, form=form)


