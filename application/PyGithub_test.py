#Simple example which prints the names of all my git repos
from application import application
from application.models import GithubUser

from github import Github

from datetime import datetime

#Retrieves all commits made by a user within a specific GitHub repository
def getCommitsInRepoByUser(username, reponame):
  # using an access token (TODO: grab by user or something)
  user = GithubUser.query.filter_by(github_username=username).first()
  print(user.github_username)
  g = Github(user.github_oauth_access_token)
  # Github Enterprise with custom hostname
  #g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
  gitUser = g.get_user()
  for repo in gitUser.get_repos():
  	print(repo.name)
  	if(repo.name == reponame):
  		return repo.get_commits(author=gitUser)

def printCommitDates(commits):
  	for commit in commits:
  		print(commit.commit.author.date)
  	return

