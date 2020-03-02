from application.models import GitHubUser, GitHubRepo, \
  GitHubCommit, GitHubPullRequest, GitHubUser, GitHubComment
from application.initialize.db_init import db
from datetime import datetime, timedelta

from github import Github
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

def capture_github_commits(startDate=datetime.min, endDate=datetime.utcnow(), user_id=None):
  '''For a given github user and time period, get all commits
     If no time range is provided, will obtain all commits since the beginning of time.
     user_id is the id row value in the github_users table. If none, will perform for all users.'''
  github_users = GitHubRepo.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  new_commits = 0
  updated_commits = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUserObject = g.get_user()
    for repo in gitUserObject.get_repos():
  	  userCommits = repo.get_commits(since=startDate, until=endDate, author=gitUserObject)
  	  for commit in userCommits:
  	  	gitCommit = GitHubCommit.query.filter_by(sha=commit.sha).first()
  	  	#TODO: calculate impact score as well
  	  	if(gitCommit is None):
  	      gitCommit = GitHubCommit(
  		    created_at=datetime.utcnow(), \
  		    updated_at=datetime.utcnow(), \
  		    github_api_repo_id=repo.id, \
  		    github_api_author_id=commit.author.id, \
  		    github_api_committer_id=commit.committer.id, \
  		    sha=commit.sha, \
  		    github_api_committed_at = commit.author.date, \
  		    insertions=commit.stats.insertions, \
  		    deletions = commit.author.deletions, \
  		    files_changed = len(commit.files)
  		    )
  		  new_commits += 1
        else:
      	  gitCommit.github_api_author_id = commit.author.id
      	  gitCommit.github_api_committer_id = commit.committer.id
      	  gitCommit.github_api_committed_at = commit.author.date
      	  gitCommit.insersions = commit.stats.insertions
      	  gitCommit.deletions = commit.author.deletions
      	  gitCommit.updated_at = datetime.utcnow()
  		  updated_commits += 1
  		#TODO: calculate edit points and impact score here  		
        db.session.add(gitCommit)


  db.session.commit()
  if(user_id is None):
    print('Added %s new github_commits to DB and updated %s github_commits for %s github_users' % (new_commits, updated_commits, len(github_users)))
  else:
    print('Added %s new github_commits to DB and updated %s github_commits for github user %s' % (new_commits, updated_commits, user_id))
  return

#We have a function to capture opened PRs.
#At some point, might be worth creating one to capture closed/merged PRs as well (as additional contributions by a user)
def capture_github_PRs_opened(startDate=datetime.min, endDate=datetime.utcnow(), user_id=None):
  '''For a given github user and time period, get all PRs the user has opened
     If no time range is provided, will obtain all PRs since the beginning of time.
     user_id is the id row value in the github_users table. If none, will perform for all users.'''
  github_users = GitHubRepo.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  new_PRs = 0
  updated_PRs = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUserObject = g.get_user()
    for repo in gitUserObject.get_repos():
      existing_repo = GitHubRepo.query.filter_by(github_api_repo_id=repo.id).one_or_none()

      if(existing_repo):
  	  userPRs = repo.get_pulls(user=gitUserObject)
  	  for pr in userPRs:
  	  	if(pr.created_at < startDate || pr.created_at > endDate):
  	  	  continue
  	  	gitPR = GitHubPullRequest.query.filter_by(github_api_pr_id=pr.id).first()
  	  	gitPR_files = pr.get_files()
  	  	#TODO: calculate impact score as well
  	  	if(gitPR is None):
  	      gitPR = GitHubCommit(
  		    created_at=datetime.utcnow(), \
  		    updated_at=datetime.utcnow(), \
  		    github_api_pr_id=pr.id, \
  		    github_api_repo_id=repo.id, \
  		    github_api_author_id=commit.author.id, \
  		    base_sha=pr.base.sha, \
  		    head_sha=pr.head.sha, \
  		    github_api_opened_at = pr.date, \
  		    insertions=pr.additions, \
  		    deletions=pr.deletions, \
  		    files_changed=changed_files, \
  		    status=pr.state
  		    )
  		  new_PRs += 1
        else:
      	  gitPR.insersions = pr.additions
      	  gitPR.deletions = pr.deletions
      	  gitPR.base_sha = pr.base.sha
  		  gitPR.head_sha = pr.head.sha
  		  gitPR.status = pr.state
      	  gitPR.updated_at = datetime.utcnow()
  		  updated_PRs += 1
  		if(pr.state == "closed"):
  		  gitPR.github_api_closed_at = pr.closed_at
  		if(pr.merged):
  		  gitPR.github_api_merged_at = pr.merged_at
  		#TODO: calculate edit points, churn percentage and impact score here
        db.session.add(gitPR)

  db.session.commit()
  if(user_id is None):
    print('Added %s new github_pull_requests to DB and updated %s github_pull_requests for %s github_users' % (new_PRS, updated_PRs, len(github_users)))
  else:
    print('Added %s new github_pull_requests to DB and updated %s github_pull_requests for github user %s' % (new_PRS, updated_PRs, user_id))
  return

def capture_github_issues():
  #TODO: For each user, get or update all a user’s open issues
  return

def capture_github_comments():
  #TODO: For each user, get all comments (and edits?) within a given time period
  return
