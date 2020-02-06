from flask import url_for, flash, redirect, request, jsonify, g, session
from flask_github import GitHub as GitHubCredentials
from flask_login import login_user, current_user, logout_user, login_required

from github import Github as GitHubUserData

from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from application.models import User, GitHubUser #TODO: add GitHub-specific models

import datetime
import requests


GITHUB_AUTH_ROUTE           = '/github-auth'
GITHUB_CALLBACK_ROUTE       = '/github-callback'
FINALIZE_GITHUB_AUTH_ROUTE  = '/api/finalize-github-auth'

GITHUB_CLIENT_ID  = Config.GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET = Config.GITHUB_CLIENT_SECRET

#Current scopes include all read access available in the API
GITHUB_SCOPES = "user, repo, read:org, read:public_key, gist, notifications, read:discussion, read:packages', read:gpg_key, workflow"


#construct GitHub object

#Using default constructor and then replicating GitHub.init_app(self, app)
#See https://github.com/cenkalti/github-flask/blob/master/flask_github.py
gitCreds = GitHubCredentials()
gitCreds.client_id = Config.GITHUB_CLIENT_ID
gitCreds.client_secret = Config.GITHUB_CLIENT_SECRET
gitCreds.base_url = 'https://api.github.com/'
gitCreds.auth_url = 'https://github.com/login/oauth/'
gitCreds.session = requests.session()


#Call to attempt to authorize a user with the GitHub API
@application.route(GITHUB_AUTH_ROUTE)
def github_auth_route():
  return gitCreds.authorize(scope=GITHUB_SCOPES)

#Invoked after github authorization attempt
@application.route(GITHUB_CALLBACK_ROUTE)
@gitCreds.authorized_handler
def authorized(oauth_token):
  if oauth_token is None:
    return flask.jsonify({ 'error: failed to retrieve an oauth token' })
  session['github_code'] = oauth_token #TODO: replace with one-time code OR more secure flask session variants 
  return redirect(FINALIZE_GITHUB_AUTH_ROUTE)


@application.route(FINALIZE_GITHUB_AUTH_ROUTE)
@login_required
def finalize_github_auth():
  oauth_token = session['github_code']
  session['github_code'] = None
  if oauth_token is None:
    return flask.jsonify({ 'error: failed to retrieve an oauth token' })
  
  #Retrieve authenticated user information and update/save to the database
  gitUserData = GitHubUserData(oauth_token).get_user()
  #Check if user exists based on their GitHub name (since it is unique to the GitHub account)
  gitUser = GitHubUser.query.filter_by(id=gitUserData.id).first()
  if gitUser is None:
    #First time user has authenticated with the app
    gitUser = GitHubUser(
      id=gitUserData.id, \
      github_oauth_access_token=oauth_token, \
      github_username=gitUserData.login, \
      github_email_address=gitUserData.email, \
      is_authenticated = True, \
      is_deleted_on_github=False, \
      created_at=gitUserData.created_at, \
      updated_at=gitUserData.updated_at, \
      user_id = current_user.id)

  else:
    gitUser.github_oauth_access_token = oauth_token
    gitUser.github_username = gitUserData.login
    gitUser.github_email_address = gitUserData.email
    gitUser.is_authenticated = True
    gitUser.is_deleted_on_github = False
    gitUser.created_at = gitUserData.created_at
    gitUser.updated_at = gitUserData.updated_at
    db.session.add(gitUser)

  db.session.add(gitUser)
  db.session.commit()

  #Update the user's access token in the database
  return redirect('/app#/settings')
