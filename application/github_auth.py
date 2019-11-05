from flask import Flask
from flask_github import GitHub
from application import application

#TODO: import GitHub models once we have some defined
#from application.models import (......)

GITHUB_INSTALL_ROUTE = '/github-install'
GITHUB_AUTH_ROUTE = '/github-auth-one'
GITHUB_CALLBACK_ROUTE = '/github-callback'

GITHUB_CLIENT_ID = application.config['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = application.config['GITHUB_CLIENT_SECRET']

#TODO: define scopes, redirect and state (current values are placeholders)
GITHUB_SCOPE = [
  'user',
  'repo'
]

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
    next_url = request.args.get('next') or url_for('index')
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect(next_url)

    user = User.query.filter_by(github_access_token=oauth_token).first()
    if user is None:
        user = User(oauth_token)
        db_session.add(user)

    #TODO: store oauth_token somewhere secure in our application
    user.github_access_token = oauth_token
    db_session.commit()
    return redirect(next_url)