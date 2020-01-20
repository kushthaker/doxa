from flask import url_for, flash, redirect, request
from flask_github import GitHub
from flask_login import login_user, current_user, logout_user, login_required

from github import Github

from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from application.models import User #TODO: add GitHub-specific models

import datetime
import requests

import pdb


GITHUB_AUTH_ROUTE = '/github-auth'
GITHUB_CALLBACK_ROUTE = '/github-callback' #homepage for now

GITHUB_CLIENT_ID = Config.GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET = Config.GITHUB_CLIENT_SECRET

#Current scopes include all read access available in the API
GITHUB_SCOPES = [
  'repo',
  'read:org',
  'read:public_key',
  'gist',
  'notifications',
  'user',
  'read:discussion'
  'read:packages',
  'read:gpg_key',
  'workflow'
  ]

#construct GitHub object

###This constructor no longer works with our current app config structure
###due to how Github-flask's app constructor is written (expects app.config['thing'] specifically)
#github = GitHub(application)

#Instead: using default GitHub() constructor and then replicating GitHub.init_app(self, app)
#See https://github.com/cenkalti/github-flask/blob/master/flask_github.py
github = GitHub()
github.client_id = Config.GITHUB_CLIENT_ID
github.client_secret = Config.GITHUB_CLIENT_SECRET
github.base_url = 'https://api.github.com/'
github.auth_url = 'https://github.com/login/oauth/'
github.session = requests.session()


#Call to attempt to authorize a user with the GitHub API
@application.route(GITHUB_AUTH_ROUTE)
def github_auth_route():
	return github.authorize(scope=GITHUB_SCOPES)

#Invoked after github authorization attempt
@application.route(GITHUB_CALLBACK_ROUTE)
@github.authorized_handler
def authorized(oauth_token):
	next_url = request.args.get('next') or url_for('home')
	if oauth_token is None:
		flash("Authorization failed.")
		return redirect(next_url)

	#TODO: retrieve authenticated user information and update/save to the database

	return redirect(next_url)
