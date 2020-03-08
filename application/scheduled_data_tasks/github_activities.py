from application.models import GitHubUser, GitHubRepo, \
  GitHubCommit, GitHubPullRequest, GitHubIssue, GitHubComment
from application.initialize.db_init import db
from datetime import datetime, timedelta

from github import Github, GithubException
from datetime import datetime, timedelta

#Used to control API request speed and avoid rate limiting problems
from time import sleep

def capture_github_repos(user_id=None):
  #For each user, or a given user, get and store all repos a user contributes to
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_repos = 0
  total_updated_repos = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUser = g.get_user()
    for repo in gitUser.get_repos():
      try:
        org = repo.organization
        org_name = org.name if org is not None else "none" 
        gitRepo = GitHubRepo.query.filter_by(github_api_repo_id=repo.id).first()
        if(gitRepo is None):
          gitRepo = GitHubRepo(
          github_api_repo_id=repo.id, \
          name=repo.name, \
          created_at=datetime.utcnow(), \
          updated_at=datetime.utcnow(), \
          github_api_owner_id = repo.owner.id, \
          organization=org_name,
          is_private=repo.private)
          total_new_repos += 1
        else:
          gitRepo.name = repo.name
          gitRepo.github_api_owner_id = repo.owner.id
          gitRepo.organization = org_name
          gitRepo.is_private = repo.private
          gitRepo.updated_at = datetime.utcnow()
          total_updated_repos += 1
        db.session.add(gitRepo)
      except Exception as e:
        print("Error adding repository with GitHub ID " + str(repo.id) + " to database.\nMessage: ")
        print(e)

  try:
    db.session.commit()
    print('Added %s new github_repos to DB and updated %s github_repos' % (total_new_repos, total_updated_repos))
  except Exception as e:
    print("Failed to commit database session.\nMessage: ")
    print(e)
    db.session.rollback()
  return



def capture_github_commits(startDate=datetime(2008,1,1), endDate=datetime.utcnow(), user_id=None):
  '''For a given github user and time period, get all commits
     If no time range is provided, will obtain all commits since the beginning of time.
     user_id is the id row value in the github_users table. If none, will perform for all users.'''
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  new_commits = 0
  updated_commits = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUser = g.get_user()
    print('capturing commits')
    for repo in gitUser.get_repos():
      try:
        sleep(2.5)
        repoBranches = repo.get_branches()
        for branch in repoBranches:
          sleep(2.5)
          userCommits = repo.get_commits(sha=branch.commit.sha, since=startDate, until=endDate, author=gitUser)
          if(userCommits is None):
            print('no commits by user ' + gitUser.name + ' in repository: ')    
            print(repo.name)
            continue    
          print(repo.name)
          for commit in userCommits:
            try:
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
                  github_api_committed_at = commit.commit.author.date, \
                  insertions=commit.stats.additions, \
                  deletions = commit.stats.deletions, \
                  files_changed = len(commit.files)
                )
                new_commits += 1
              else:
                gitCommit.github_api_author_id = commit.author.id
                gitCommit.github_api_committer_id = commit.committer.id
                gitCommit.github_api_committed_at = commit.commit.author.date
                gitCommit.insersions = commit.stats.additions
                gitCommit.deletions = commit.stats.deletions
                gitCommit.updated_at = datetime.utcnow()
                updated_commits += 1
              #TODO: calculate edit points and impact score here      
              db.session.add(gitCommit)
            except Exception as e:
              print("Error adding commit with GitHub ID " + str(commit.sha) + " to database.\nMessage: ")
              print(e)
            else:
              print("Successfully updated commit with GitHub ID " + str(commit.sha) + " in database.\n")
      except GithubException as e:
        print(e.args[1]['message'] + " Skipping.")
        continue

  try:
    db.session.commit()
    if(user_id is None):
      print('Added %s new github_commits to DB and updated %s github_commits for %s github_users' % (new_commits, updated_commits, len(github_users)))
    else:
      print('Added %s new github_commits to DB and updated %s github_commits for github user %s' % (new_commits, updated_commits, user_id))
  except Exception as e:
    print("Failed to commit database.\nMessage: ")
    print(e)
    db.session.rollback()

  return

#For regular updates (1min grace to avoid missing data)
def capture_gitcommits_1hr():
  nowtime = datetime.utcnow()
  capture_github_commits(startDate=nowtime-timedelta(hours=2), endDate=datetime.utcnow())

#Less frequent lookback job to check for rewrites or missed data
def capture_gitcommits_30day():
  nowtime = datetime.utcnow()
  capture_github_commits(startDate=nowtime-timedelta(days=30), endDate=datetime.utcnow())  



#We have a function to capture opened PRs.
#At some point, might be worth capturing closed/merged PRs as well (as additional contributions by a user)
def capture_github_prs_opened(startDate=datetime(2008,1,1), endDate=datetime.utcnow(), user_id=None):
  '''For a given github user and time period, get all PRs the user has opened
     If no time range is provided, will obtain all PRs since the beginning of time.
     user_id is the id row value in the github_users table. If none, will perform for all users.'''
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  new_PRs = 0
  updated_PRs = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUser = g.get_user()
    for repo in gitUser.get_repos():
      sleep(2.5)      
      userPRs = repo.get_pulls()
      for pr in userPRs:
        try:
          if (pr.created_at < startDate or pr.created_at > endDate):
            continue
          if(pr.user.id != gitUser.id):
            continue
          gitPR = GitHubPullRequest.query.filter_by(github_api_pr_id=pr.id).first()
          sleep(2.5)
          gitPR_files = pr.get_files()
          #TODO: calculate impact score as well
          if(gitPR is None):
            gitPR = GitHubPullRequest(
              created_at=datetime.utcnow(),
              updated_at=datetime.utcnow(),
              github_api_pr_id=pr.id,
              github_api_repo_id=repo.id,
              github_api_author_id=pr.user.id,
              base_sha=pr.base.sha,
              head_sha=pr.head.sha,
              github_api_opened_at = pr.created_at,
              insertions=pr.additions,
              deletions=pr.deletions,
              files_changed=pr.changed_files,
              status=pr.state
            )
            new_PRs += 1
          else:
            gitPR.insersions = pr.additions
            gitPR.deletions = pr.deletions
            gitPR.files_changed = pr.changed_files
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
        except Exception as e:
          print("Error adding PR with GitHub ID " + str(pr.id) + " to database.\nMessage: ")
          print(e)

  try:
    db.session.commit()
    if(user_id is None):
      print('Added %s new github_pull_requests to DB and updated %s github_pull_requests for %s github_users' % (new_PRs, updated_PRs, len(github_users)))
    else:
      print('Added %s new github_pull_requests to DB and updated %s github_pull_requests for github user %s' % (new_PRs, updated_PRs, user_id))
  except Exception as e:
    print("Failed to commit database.\nMessage: ")
    print(e)
    db.session.rollback()

  return

#For regular updates (1min grace to avoid missing data)
def capture_opened_prs_1hr():
  nowtime = datetime.utcnow()
  capture_github_prs_opened(startDate=nowtime-timedelta(hours=2), endDate=datetime.utcnow())

#Less frequent lookback job to check for rewrites or missed data
def capture_opened_prs_30day():
  nowtime = datetime.utcnow()
  capture_github_prs_opened(startDate=nowtime-timedelta(days=30))



def capture_github_issues(startDate=datetime(2008,1,1), user_id=None):
  #For each user, or for a single specified user, get or update all issues the user has opened or closed
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_issues = 0
  total_updated_issues = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUser = g.get_user()
    for repo in gitUser.get_repos():
      #Step 1: issues opened by user
      sleep(2.5)      
      for issue in repo.get_issues(since=startDate, creator=gitUser.name):
        try:
          if(issue is None):
            continue
          if(issue.user is None):
            continue
          issue_open = True if issue.state == "closed" else False
          #Only add issues to the databse if the current user created the issue
          if (issue.user.id != gitUser.id):
            continue
          gitIssue = GitHubIssue.query.filter_by(github_api_issue_id=issue.id).first()      
          if(gitIssue is None):
            gitIssue = GitHubIssue(
              created_at=datetime.utcnow(),
              updated_at=datetime.utcnow(),
              github_api_issue_id=issue.id,
              github_api_creator_id = issue.user.id,
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
        except Exception as e:
          print("Error adding issue with GitHub ID " + str(issue.id) + " to database.\nMessage: ")
          print(e)

  try:
    db.session.commit()
    print('Added %s new github_issues to DB and updated %s github_issues' % (total_new_issues, total_updated_issues))
  except Exception as e:
    print("Failed to commit database.\nMessage: ")
    print(e)
    db.session.rollback()

  return

#For regular updates (1min grace to avoid missing data)
def capture_gitissues_1hr():
  nowtime = datetime.utcnow()
  capture_github_issues(startDate=nowtime-timedelta(hours=2))

#Less frequent lookback job to check for rewrites or missed data
def capture_gitissues_30day():
  nowtime = datetime.utcnow()
  capture_github_issues(startDate=nowtime-timedelta(days=30))



def capture_github_issue_comments(startDate=datetime(2008,1,1), user_id=None):
  #TODO: For each user, get all issue comments within a given time period
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_comments = 0
  total_updated_comments = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUser = g.get_user()
    for repo in gitUser.get_repos():
      #Step 1: issues opened by user
      sleep(2.5)      
      for issue in repo.get_issues(since=startDate):
        #could have comments on older issues
        print('getting issue in repo ' + repo.name)
        sleep(2.5)      
        for comment in issue.get_comments(since=startDate):
          try:
            #only update comments written by the user
            if(comment.user.id != gitUser.id):
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
          except Exception as e:
            print("Error adding (issue) comment with GitHub ID " + str(comment.id) + " to database.\nMessage: ")
            print(e)
          else:
            print('comment added')

  try:
    db.session.commit()
    print('Added %s new (issue) comments to DB and updated %s (issue) comments' % (total_new_comments, total_new_comments))
  except Exception as e:
    print("Failed to commit database.\nMessage: ")
    print(e)
    db.session.rollback()  
  return

#For regular updates (1min grace to avoid missing data)
def capture_gitIssueComments_1hr():
  nowtime = datetime.utcnow()
  capture_github_issue_comments(startDate=nowtime-timedelta(hours=2))

#Less frequent lookback job to check for rewrites or missed data
def capture_gitIssueComments_30day():
  nowtime = datetime.utcnow()
  capture_github_issue_comments(startDate=nowtime-timedelta(days=30))



def capture_github_pr_comments(startDate=datetime(2008,1,1), user_id=None):
  #TODO: For each user, get all PR comments within a given time period
  github_users = GitHubUser.query.all() if user_id is None else GitHubUser.query.filter_by(id=user_id)
  total_new_comments = 0
  total_updated_comments = 0
  for user in github_users:
    g = Github(user.github_oauth_access_token)
    gitUser = g.get_user()
    for repo in gitUser.get_repos():
      sleep(2.5)            
      for pr in repo.get_pulls():
        for comment in pr.get_review_comments(since=startDate):
          try:
            #only update comments written by the user
            if(comment.user.id != gitUser.id):
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
          except Exception as e:
            print("Error adding (PR) comment with GitHub ID " + str(comment.id) + " to database.\nMessage: ")
            print(e)
          else:
            print('added or updated' + str(total_new_comments + total_updated_comments) ' comments.')

  try:
    db.session.commit()
    print('Added %s new (PR) comments to DB and updated %s (PR) comments' % (total_new_comments, total_new_comments))
  except Exception as e:
    print("Failed to commit database.\nMessage: ")
    print(e)
    db.session.rollback()  
  return

#For regular updates (1min grace to avoid missing data)
def capture_gitPRComments_1hr():
  nowtime = datetime.utcnow()
  capture_github_pr_comments(startDate=nowtime-timedelta(hours=2))

#Less frequent lookback job to check for rewrites or missed data
def capture_gitPRComments_30day():
  nowtime = datetime.utcnow()
  capture_github_pr_comments(startDate=nowtime-timedelta(days=30))
