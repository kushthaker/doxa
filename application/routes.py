from flask import render_template, url_for, flash, redirect, request
from application import application
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post, RawSlackEvent

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
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created for %s!' % form.username.data, 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@application.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'abc@eee.com' and form.password.data == 'password':
			flash('Login successful for %s' % form.email.data, 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check user and pass', 'danger')
	return render_template('login.html', title='Login', form=form)
