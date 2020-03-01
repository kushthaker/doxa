from application.models import GitHubUser, GitHubRepo, \
  GitHubCommit, GitHubPullRequest, GitHubUser, GitHubComment
from application.initialize.db_init import db
from datetime import datetime, timedelta


def capture_github_repos():
	#TODO: For each user, get and store all repos a user contributes to
	return

def capture_github_commits():
	#TODO: For each user, get all the user’s commits in a given time period
	return

def capture_github_PRs():
	#TODO: For each user, get or update all the user’s unmerged PRs
	return

def capture_github_issues():
	#TODO: For each user, get or update all a user’s open issues
	return

def capture_github_comments():
	#TOOD: For each user, get all comments (and edits?) within a given time period
	return
