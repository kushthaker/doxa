from flask import url_for, flash, redirect, request
from flask_github import GitHub

from github import Github

from application import application, PyGithub_test, db
from application.models import GithubUser

import datetime

import pdb

#from application.models import <github models> #add this later
GITHUB_AUTH_ROUTE = '/github-auth'
GITHUB_CALLBACK_ROUTE = '/github-callback' #homepage for now

GITHUB_CLIENT_ID = application.config['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = application.config['GITHUB_CLIENT_SECRET']
#TODO: define more scopes, redirect and state (current values are placeholders)
GITHUB_SCOPES = "user, repo, read:discussion"

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

	gitUserData = Github(oauth_token).get_user()
	#Check if user exists based on their GitHub name (since it is unique to the GitHub account)
	gitUser = GithubUser.query.filter_by(id=gitUserData.id).first()
	if gitUser is None:
		#First time user has authenticated with the app
		#TODO: setup other model information here (can probably do this with PyGithub)
		gitUser = GithubUser(
												github_oauth_access_token=oauth_token, \
												is_authenticated = True)
		gitUser.is_authenticated = True;
		print("New user authenticated!")


  #Update the user's access token in the database
	gitUser.github_oauth_access_token = oauth_token
	gitUser.id = gitUserData.id
	#gitUser.github_org_id = github.Organization.Organization.id in gitUserData.getOrgs().id
	gitUser.github_username = gitUserData.name
	gitUser.github_email_address = gitUserData.email
	gitUser.created_date = gitUserData.created_at
	gitUser.last_updated = gitUserData.updated_at
	db.session.add(gitUser)
	db.session.commit()

	return redirect(next_url)

#Clears all GithubUser rows in the db (for local testing purposes)
#@application.route('/clear-github')
#def clearGitUsers():
#	users = GithubUser.query.all()
#	if(users is not None):
#		print(users)
#	else:
#		print("Empty")
#	GithubUser.query.delete()
#	db.session.commit()
#	return redirect('/')

@application.route('/github-test')
def listCommitDates():
	#TODO: replace "Callum" with a specified Github user (may want to filter by an ID instead)
	gitUser = GithubUser.query.filter_by(github_username="Callum").first()
	if gitUser is not None:
		sixMonthsAgo = datetime.datetime.now() - datetime.timedelta(6*365/12)
		PyGithub_test.printUserCommits(gitUser.id, sixMonthsAgo)
	return redirect('/')
