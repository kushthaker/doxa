from flask import Flask, render_template, url_for

application = Flask(__name__)
app = application

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
@app.route("/cheese")
@app.route("/fromage")
def hello():         
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title="about")

if __name__ == "__main__":
    app.debug = True         
    app.run()


