from flask import url_for, flash, redirect, request, jsonify, g
from flask_github import GitHub as GitHubCredentials
from flask_login import login_user, current_user, logout_user, login_required

from github import Github as GitHubUserData
from application.forms import GithubAuthorizationForm
from application.initialize.config import Config
from application.app_setup import application
from application.initialize.db_init import db
from application.models import User, GitHubUser #TODO: add GitHub-specific models
from application.utils.route_utils import token_required


import datetime
import requests

import pdb


GITHUB_AUTH_ROUTE = '/github-auth'
GITHUB_CALLBACK_ROUTE = '/github-callback' #homepage for now

GITHUB_CLIENT_ID = Config.GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET = Config.GITHUB_CLIENT_SECRET

#Current scopes include all read access available in the API
GITHUB_SCOPES = "user, repo, read:org, read:public_key, gist, notifications, read:discussion, read:packages', read:gpg_key, workflow"


#construct GitHub object

###This constructor no longer works with our current app config structure
###due to how Github-flask's app constructor is written (expects app.config['thing'] specifically)
#github = GitHub(application)

#Instead: using default constructor and then replicating GitHub.init_app(self, app)
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
    flash("Authorization failed.")
    return redirect('/app#/settings')
  
  return redirect('/app#/github-auth/%s' % oauth_token)


@application.route('/api/finalize-github-auth', methods=['POST'])
@token_required
def finalize_github_auth(current_user):
  #next_url = request.args.get('next') or url_for('home')
  auth_form = GithubAuthorizationForm()
  oauth_token = auth_form.data.get('code')
  #Retrieve authenticated user information and update/save to the database
  gitUserData = GitHubUserData(oauth_token).get_user()
  #Check if user exists based on their GitHub name (since it is unique to the GitHub account)
  gitUser = GitHubUser.query.filter_by(id=gitUserData.id).first()
  if gitUser is None:
    #First time user has authenticated with the app
    #TODO: setup other model information here (can probably do this with PyGithub)
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
    
    print("New user authorized!")

  else:
    gitUser.github_oauth_access_token = oauth_token
    gitUser.github_username = gitUserData.login
    gitUser.github_email_address = gitUserData.email
    gitUser.is_authenticated = True
    gitUser.is_deleted_on_github = False
    gitUser.created_at = gitUserData.created_at
    gitUser.updated_at = gitUserData.updated_at
    db.session.add(gitUser)
    print("Authorization updated!")

  db.session.add(gitUser)
  db.session.commit()

  #Update the user's access token in the database
  flash("Authorization successful.")
  print(current_user.user_details())
  return jsonify(current_user.user_details())
