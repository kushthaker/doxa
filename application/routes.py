import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, send_from_directory, Response
from application.initialize.bcrypt_init import bcrypt
from application.initialize.db_init import db
from application.initialize.scheduler_jobstore_init import scheduler as apscheduler
from application.app_setup import application
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, ChangePasswordForm
from application.models import User, Post, RawSlackEvent
from flask_login import login_user, current_user, logout_user, login_required
from application import slack_auth
from application import google_auth
from application import github_auth
from application.scheduled_data_tasks import apscheduler_util
from flask_wtf import csrf
import jwt
from flask import session
from datetime import datetime, timedelta
from application.applied_science.data_annotation import labelled_focus_time_df

# this should eventually be replaced by a CDN
@application.route('/app', methods=['GET'])
def app():
	return send_from_directory('doxa-frontend/dist/', 'index.html')

@application.route('/static_files/js/<path:filename>', methods=['GET'])
def send_static_js(filename):
	return send_from_directory('doxa-frontend/dist/static_files/js', filename)

@application.route('/static_files/css/<path:filename>', methods=['GET'])
def send_static_css(filename):
	return send_from_directory('doxa-frontend/dist/static_files/css', filename)

@application.route('/static_files/img/<path:filename>', methods=['GET'])
def send_static_img(filename):
	return send_from_directory('doxa-frontend/dist/static_files/img', filename)

@application.route('/static_files/<path:filename>', methods=['GET'])
def send_static_favicon(filename):
	return send_from_directory('doxa-frontend/dist/static_files', 'favicon.png')

@application.route('/favicon.ico', methods=['GET'])
def send_favicon():
	return send_from_directory('doxa-frontend/dist/static_files', 'favicon.png')

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

@application.route('/api/check-login', methods=['GET'])
def logged_in():
	if current_user.is_authenticated:
		return jsonify(current_user.to_dict())
	return jsonify(None)

@application.route('/api/login', methods=['POST'])
def api_login_2():
	form = LoginForm()
	user = User.query.filter_by(email=form.email.data).first()
	if user and bcrypt.check_password_hash(user.password, form.password.data):
		login_user(user, True)
		print(session)
		response = user.to_dict()
		response['authenticated'] = True
		return jsonify(response)
	response = form.errors
	response['errors'] = { 'Credentials': ['Login unsuccessful. Please check email and password.'] }
	return jsonify(response), 401

@application.route('/api/logout', methods=['GET'])
def api_logout():
	if current_user.is_authenticated:
		logout_user()
		return jsonify(True)
	return jsonify({ 'errors': { 'Logout': ['No user is logged in.']}}), 401


@application.route('/api/users', methods=['GET'])
def api_users():
	users = User.query.all()
	response = jsonify([user.to_dict() for user in users])
	return response

@application.route('/api/users/<int:user_id>', methods=['GET'])
def api_user(user_id):
	user = User.query.get_or_404(user_id)
	return jsonify(user.to_dict())

@application.route('/api/get_csrf', methods=['GET'])
def api_get_csrf():
	csrf_token = csrf.generate_csrf()
	return jsonify({ 'csrf_token':  csrf_token})

@application.route('/api/user_details', methods=['GET'])
@login_required
def user_details():
	return jsonify(current_user.user_details())

@application.route('/api/change-password', methods=['POST'])
@login_required
def api_change_password():
	form = ChangePasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
		current_user.password = hashed_password
		db.session.add(current_user)
		db.session.commit()
		return jsonify({ 'Response': 'Password successfully changed' })
	response = {}
	response['errors'] = form.errors
	return jsonify(response), 401

@application.route('/api/register', methods=['POST'])
def api_register():
	form = RegistrationForm()
	user = User(username=form.username.data, email=form.email.data)
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')	
		user.password = hashed_password
		db.session.add(user)
		db.session.commit()
		return jsonify(user.to_dict())
	response = user.to_dict()
	response['errors'] = form.errors
	return jsonify(response), 401

@application.route('/api/activity-data', methods=['GET'])
@login_required
def activity_data():
	# can build the _collaborative activity_ calculation, streaks, etc. on top of this
	activity_df = labelled_focus_time_df(current_user)
	return Response(activity_df.to_json(orient='records', date_format='iso'), mimetype='application/json')
	# return jsonify([data.to_json() for data in current_user.activity_report_data][:20])

@application.route("/")
def home():
	image_path = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/07-User-Account-Profile-Pic/flaskblog/static/profile_pics/default.jpg'
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
	return render_template('home.html', posts=posts, image_path=image_path)

@application.route("/about")
def about():
	return render_template('about.html', title="About")

@application.route("/register", methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		if request.is_json:
			return jsonify(current_user.to_dict())
		return redirect(url_for('home'))
	form = RegistrationForm()
	
	user = User(username=form.username.data, email=form.email.data)
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')	
		user.password = hashed_password
		db.session.add(user)
		db.session.commit()
		flash('Account created for %s!' % form.username.data, 'success')
		if request.is_json:
			print(user.to_dict())
			return jsonify(user.to_dict())
		return redirect(url_for('home'))
	print(form.errors)
	if request.is_json:
		response = user.to_dict()
		response['errors'] = form.errors
		return jsonify(response), 401
	return render_template('register.html', title='Register', form=form)

@application.route("/login", methods=['GET','POST'])
def login():
	if request.is_json:
		if current_user.is_authenticated:
			return jsonify({ 'authenticated': True })
		else:
			form = LoginForm()
			user = User.query.filter_by(email=form.email.data).first()
			if user and bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				return jsonify({ 'authenticated': True })
			response = form.errors
			form['authenticated'] = False
			return jsonify(response)

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
	output_size = (125,125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
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

@application.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('You post was created', 'success')
		return(redirect(url_for('home')))
	return render_template('create_post.html', title='New Post', form=form, legend='New Post')

@application.route("/post/<int:post_id>")
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title=post.title, post=post)

@application.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash('Post updated!', 'success')
		return redirect(url_for('post', post_id=post.id))
	elif request.method == 'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create_post.html', title='Update Post', legend='Update Post', form=form)

@application.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Post deleted!', 'success')
	return redirect(url_for('home'))

@application.route("/user/<string:username>")
def user_posts(username):
	page = request.args.get('page', 1, type=int)
	user = User.query.filter_by(username=username).first_or_404()
	posts = Post.query.filter_by(author=user)\
		.order_by(Post.date_posted.desc())\
		.paginate(page=page, per_page=3)
	return render_template('home.html', posts=posts, user=user)
