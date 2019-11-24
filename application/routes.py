import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from application import application, db, bcrypt
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from application.models import User, Post, RawSlackEvent
from flask_login import login_user, current_user, logout_user, login_required
from application import slack_auth
from application import apscheduler_util
from application import scheduler as apscheduler

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

@application.route('/test-scheduling-route', methods=['GET'])
def test_scheduling_route():
	trigger = apscheduler_util.build_minute_trigger(3)
	function = apscheduler_util.test_running_task
	job_schedule_result = apscheduler_util.add_or_update_job_from_function(apscheduler, func=function, trigger=trigger)
	return str(job_schedule_result) # test method to see if scheduled job is working in production

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



