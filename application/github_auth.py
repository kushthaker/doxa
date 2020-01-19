from flask import url_for, flash, redirect, request
from flask_github import GitHub
from flask_login import login_user, current_user, logout_user, login_required

from github import Github

from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from application.models import User #TODO: add GitHub-specific models later

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

GITHUB_REDIRECT_URI = None
GITHUB_STATE = None

#construct GitHub object

###This line no longer works with our current app config structure
###due to Github-flask having an amateurishly inflexible app constructor
#github = GitHub(application)

#Manual setup
github = GitHub()
github.client_id = Config.GITHUB_CLIENT_ID
github.client_secret = Config.GITHUB_CLIENT_SECRET
github.base_url = 'https://api.github.com/'
github.auth_url = 'https://github.com/login/oauth/'
github.session = requests.session()


#Call to attempt to authorize a user with the GitHub API
@application.route(GITHUB_AUTH_ROUTE)
def github_auth_route():
	#pdb.set_trace()
	return github.authorize(scope=GITHUB_SCOPES)

#Invoked after github authorization attempt
@application.route(GITHUB_CALLBACK_ROUTE)
@github.authorized_handler
def authorized(oauth_token):
	next_url = request.args.get('next') or url_for('home')
	if oauth_token is None:
		flash("Authorization failed.")
		return redirect(next_url)

	#TODO: retrieve authenticated user information and save to the database

	#gitUserData = Github(oauth_token).get_user()
	#Check if user exists based on their GitHub name (since it is unique to the GitHub account)
	#gitUser = GithubUser.query.filter_by(id=gitUserData.id).first()
	# if gitUser is None:
		#First time user has authenticated with the app
		#TODO: setup other model information here (can probably do this with PyGithub)
		# gitUser = GithubUser(
		# 										github_oauth_access_token=oauth_token, \
		# 										is_authenticated = True)
		# gitUser.is_authenticated = True;
		# print("New user authenticated!")

	#Update the user's access token in the database
	# gitUser.github_oauth_access_token = oauth_token
	# gitUser.id = gitUserData.id
	#gitUser.github_org_id = github.Organization.Organization.id in gitUserData.getOrgs().id
	# gitUser.github_username = gitUserData.name
	# gitUser.github_email_address = gitUserData.email
	# gitUser.created_date = gitUserData.created_at
	# gitUser.last_updated = gitUserData.updated_at
	# db.session.add(gitUser)
	# db.session.commit()

	return redirect(next_url)