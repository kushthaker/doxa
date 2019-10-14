from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

application = Flask(__name__)
app = application
app.config['SECRET_KEY'] = '7a273729d601733097ead8f655a410eb'


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
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.email.data == 'abc@eee.com' and form.password.data == 'password':
		flash(f'Login successful for {form.email.data}', 'success')
		return redirect(url_for('home'))
	else:
		flash(f'Login unsuccessful. Please check user and pass', 'danger')
	return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.debug = True         
    app.run()


