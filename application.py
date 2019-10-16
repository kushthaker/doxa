from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

application = Flask(__name__) # aws eb requires 'application' name for Flask instance
app = application

app.config['SECRET_KEY'] = '7a273729d601733097ead8f655a410eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return "User('%s','%s','%s')" % (self.username, self.email, self.image_file)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Post('%s', '%s')" % (self.title, self.date_posted)



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

@app.route("/")
def home():         
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title="About")


@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created for %s!' % form.username.data, 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'abc@eee.com' and form.password.data == 'password':
			flash('Login successful for %s' % form.email.data, 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check username and pass', 'danger')
	return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.debug = True         
    app.run()


