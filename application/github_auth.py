from flask import url_for, flash, redirect, request
from flask_github import GitHub

from github import Github

from application import application, PyGithub_test
from application.models import GithubUser

import pdb

#from application.models import <github models> #add this later
GITHUB_AUTH_ROUTE = '/github-auth'
GITHUB_CALLBACK_ROUTE = '/github-callback' #homepage for now

GITHUB_CLIENT_ID = application.config['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = application.config['GITHUB_CLIENT_SECRET']
#TODO: define more scopes, redirect and state (current values are placeholders)
GITHUB_SCOPES = "user, repo"

GITHUB_REDIRECT_URI = None
GITHUB_STATE = None

github = GitHub(application)

#Call to attempt to authorize a user with the GitHub API
@application.route(GITHUB_AUTH_ROUTE)
def github_auth_route():
	return github.authorize(scope=GITHUB_SCOPES, redirect_uri=GITHUB_REDIRECT_URI, state=GITHUB_STATE)

#Invoked after github authorization attempt
@application.route(GITHUB_CALLBACK_ROUTE)
@github.authorized_handler
def authorized(oauth_token):
	next_url = request.args.get('next') or url_for('home')
	if oauth_token is None:
		flash("Authorization failed.")
		return redirect(next_url)

	gitUser = GithubUser.query.filter_by(github_oauth_access_token=oauth_token).first()

	if gitUser is None:
		#First time user has authenticated with the app
		#TODO: setup other model information here (can probably do this with PyGithub)
		gitUser = GithubUser(
												github_oauth_access_token=oauth_token, \
												is_authenticated = True)
		gitUser.is_authenticated = True;

  #Update the user's access token in the database
	gitUser.github_oauth_access_token = oauth_token
	gitUserData = Github(oauth_token).get_user()
	gitUser.id = gitUserData.id
	#gitUser.github_org_id = github.Organization.Organization.id in gitUserData.getOrgs().id
	gitUser.github_username = gitUserData.name
	gitUser.github_email_address = gitUserData.email
	gitUser.created_date = gitUserData.created_at
	gitUser.last_updated = gitUserData.updated_at
	gitUser.save()

	return redirect(next_url)

@application.route('/github-test')
def listCommitDatesTest():
	commitList = PyGithub_test.getCommitsInRepoByUser("Callum", "Minotaur")
	PyGithub_test.printCommitDates(commitList)
	return redirect('/')
