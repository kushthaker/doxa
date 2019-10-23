from flask import render_template, url_for, flash, redirect, request
from application import application, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post, RawSlackEvent
from flask_login import login_user, current_user, logout_user, login_required

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


@application.route("/account")
@login_required
def account():
	return render_template('account.html', title='Account')
