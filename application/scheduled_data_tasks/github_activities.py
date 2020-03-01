from application.models import GitHubUser, GitHubRepo, \
  GitHubCommit, GitHubPullRequest, GitHubUser, GitHubComment
from application.initialize.db_init import db
from datetime import datetime, timedelta

from github import Github
import PyGithub as PyGit
from datetime import datetime

def capture_github_repos():
  #For each user, get and store all repos a user contributes to
  github_users = GitHubUser.query.all()
  total_new_repos = 0
  total_updated_repos = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    for repo in g.get_user().get_repos():
      gitRepo = GitHubRepo.query.filter_by(github_api_repo_id=repo.id).first()
      if(gitRepo is None):
  	    gitRepo = GitHubRepo(
  		  github_api_repo_id=repo.id, \
  		  name=repo.name, \
  		  created_at=datetime.utcnow(), \
  		  updated_at=datetime.utcnow(), \
  		  github_api_owner_id = repo.owner.id, \
  		  organization=repo.organization.name,
  		  is_private=repo.private)
  		total_new_repos += 1
      else:
      	gitRepo.name = repo.name
      	gitRepo.github_api_owner_id = repo.owner.id
      	gitRepo.organization = repo.organization.name
      	gitRepo.is_private = repo.private
      	gitRepo.updated_at = datetime.utcnow()
  		total_updated_repos += 1
      db.session.add(gitRepo)

  db.session.commit()
  print('Added %s new github_repos to DB and updated %s github_repos' % (total_new_repos, total_updated_repos))
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
  #TODO: For each user, get all comments (and edits?) within a given time period
  return
