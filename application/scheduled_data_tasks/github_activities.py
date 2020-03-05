from application.models import GitHubUser, GitHubRepo, \
  GitHubCommit, GitHubPullRequest, GitHubUser, GitHubComment
from application.initialize.db_init import db
from datetime import datetime, timedelta

from github import Github
from datetime import datetime

def capture_github_repos(user_id=None):
  #For each user, or a given user, get and store all repos a user contributes to
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
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
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
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

#For regular updates (1min grace to avoid missing data)
def capture_gitcommits_10min():
  nowtime = datetime.utcnow()
  capture_github_commits(startDate=nowtime-datetime.timedelta(minutes=11), endDate=datetime.utcnow()):

#Less frequent lookback job to check for rewrites or missed data
def capture_gitcommits_history():
  nowtime = datetime.utcnow()
  capture_github_commits(startDate=nowtime-datetime.timedelta(days=30), endDate=datetime.utcnow(), None):  



#We have a function to capture opened PRs.
#At some point, might be worth capturing closed/merged PRs as well (as additional contributions by a user)
def capture_github_prs_opened(startDate=datetime.min, endDate=datetime.utcnow(), user_id=None):
  '''For a given github user and time period, get all PRs the user has opened
     If no time range is provided, will obtain all PRs since the beginning of time.
     user_id is the id row value in the github_users table. If none, will perform for all users.'''
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  new_PRs = 0
  updated_PRs = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    g_user = g.get_user()
    for repo in g_user.get_repos():
      userPRs = repo.get_pulls(user=g_user)
      for pr in userPRs:
        if (pr.created_at < startDate or pr.created_at > endDate):
          continue
        gitPR = GitHubPullRequest.query.filter_by(github_api_pr_id=pr.id).first()
        gitPR_files = pr.get_files()
        #TODO: calculate impact score as well
        if(gitPR is None):
          gitPR = GitHubCommit(
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            github_api_pr_id=pr.id,
            github_api_repo_id=repo.id,
            github_api_author_id=commit.author.id,
            base_sha=pr.base.sha,
            head_sha=pr.head.sha,
            github_api_opened_at = pr.created_at,
            insertions=pr.additions,
            deletions=pr.deletions,
            files_changed=changed_files,
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

#For regular updates (1min grace to avoid missing data)
def capture_opened_prs_10min():
  nowtime = datetime.utcnow()
  capture_github_prs_opened(startDate=nowtime-datetime.timedelta(minutes=11), endDate=datetime.utcnow()):

#Less frequent lookback job to check for rewrites or missed data
def capture_opened_prs_history():
  capture_github_prs_opened():



def capture_github_issues(startDate=datetime.min, user_id=None):
  #For each user, or for a single specified user, get or update all issues the user has opened or closed
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_issues = 0
  total_updated_issues = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    g_user = g.get_user()
    for repo in g_user.get_repos():
      #Step 1: issues opened by user
      for issue in repo.get_issues(since=startDate):
        issue_open = True if issue.state == "closed" else False
        #Only add issues to the databse if the current user either created or closed the issue
        if (issue.creator.id != g_user.id and (issue_open or issue.closed_by.id != g_user.id)):
          continue
        gitIssue = GitHubIssue.query.filter_by(github_api_issue_id=issue.id).first()      
        if(gitIssue is None):
          gitIssue = GitHubIssue(
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            github_api_issue_id=issue.id,
            github_api_creator_id = issue.creator.id,
            github_api_opened_at=issue.created_at,
            is_open=issue_open
          )
          total_new_issues += 1
        else:
          gitIssue.is_open = issue_open
          gitIssue.updated_at = datetime.utcnow()
          total_updated_issues += 1
        if(issue.state == "closed"):
          gitIssue.github_api_closed_at = issue.closed_at
          gitIssue.github_api_closer_id = issue.closed_by.id
        #TODO: calculate and update impact score of opening and closing
        db.session.add(gitIssue)

  db.session.commit()
  print('Added %s new github_issues to DB and updated %s github_issues' % (total_new_issues, total_updated_issues))
  return

#For regular updates (1min grace to avoid missing data)
def capture_gitissues_10min():
  nowtime = datetime.utcnow()
  capture_github_issues(startDate=nowtime-datetime.timedelta(minutes=10))

#Less frequent lookback job to check for rewrites or missed data
def capture_gitissues_history():
  capture_github_issues()



def capture_github_issue_comments(startDate=datetime.min, user_id=None):
  #TODO: For each user, get all issue comments within a given time period
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_comments = 0
  total_updated_comments = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    g_user = g.get_user()
    for repo in g_user.get_repos():
      #Step 1: issues opened by user
      for issue in repo.get_issues():
        #could have comments on older issues
        for comment in issue.get_comments(since=startDate):
          #only update comments written by the user
          if(comment.user.id != g_user.id):
            continue
          gitComment = GitHubComment.query.filter_by(github_api_comment_id=comment.id).first()
          if(gitComment is None):
            gitComment = GitHubComment(
              created_at=datetime.utcnow(),
              updated_at=datetime.utcnow(),
              comment_type="issue",
              github_api_comment_id=comment.id,
              github_api_author_id=comment.user.id,
              github_api_parent_id=issue.id,
              github_api_written_at=comment.created_at,
              github_api_edited_at=comment.updated_at,
            )
            total_new_comments += 1
          else:
            gitComment.github_api_edited_at = comment.updated_at
            gitComment.updated_at = datetime.utcnow()
            total_updated_comments += 1
          #TODO: calculate and update impact score of comment
          db.session.add(gitComment)

  db.session.commit()
  print('Added %s new (issue) comments to DB and updated %s (issue) comments' % (total_new_comments, total_new_comments))
  return

#For regular updates (1min grace to avoid missing data)
def capture_gitIssueComments_10min():
  nowtime = datetime.utcnow()
  capture_github_issue_comments(startDate=nowtime-datetime.timedelta(minutes=11))

#Less frequent lookback job to check for rewrites or missed data
def capture_gitIssueComments_history():
  capture_github_issue_comments()



def capture_github_pr_comments(startDate=datetime.min, user_id=None):
  #TODO: For each user, get all PR comments within a given time period
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_comments = 0
  total_updated_comments = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    g_user = g.get_user()
    for repo in g_user.get_repos():
      for pr in repo.get_pulls():
        for comment in pr.get_comments(since=startDate):
          #only update comments written by the user
          if(comment.user.id != g_user.id):
            continue
          gitComment = GitHubComment.query.filter_by(github_api_comment_id=comment.id).first()
          if(gitComment is None):
            gitComment = GitHubComment(
              created_at=datetime.utcnow(),
              updated_at=datetime.utcnow(),
              comment_type="PR",
              github_api_comment_id=comment.id,
              github_api_author_id=comment.user.id,
              github_api_parent_id=pr.id,
              github_api_written_at=comment.created_at,
              github_api_edited_at=comment.updated_at,
            )
            total_new_comments += 1
          else:
            gitComment.github_api_edited_at = comment.updated_at
            gitComment.updated_at = datetime.utcnow()
            total_updated_comments += 1
          #TODO: calculate and update impact score of comment
          db.session.add(gitComment)

  db.session.commit()
  print('Added %s new (PR) comments to DB and updated %s (PR) comments' % (total_new_comments, total_new_comments))
  return

#For regular updates (1min grace to avoid missing data)
def capture_gitPRComments_10min():
  nowtime = datetime.utcnow()
  capture_github_pr_comments(startDate=nowtime-datetime.timedelta(minutes=11))

#Less frequent lookback job to check for rewrites or missed data
def capture_gitPRComments_history():
  capture_github_pr_comments()
