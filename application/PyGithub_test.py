#Simple example which prints the names of all my git repos
from application import application
from application.models import GithubUser

from github import Github

from datetime import datetime

#Retrieves all commits made by a user within a specific GitHub repository
def printUserCommits(githubId, startDate):
  # using an access token (TODO: grab by user or something)
  user = GithubUser.query.filter_by(id=githubId).first()
  g = Github(user.github_oauth_access_token)
  # Github Enterprise with custom hostname
  #g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
  gitUser = g.get_user()

  startDateString = startDate.strftime("%m/%d/%Y, %H:%M:%S")
  print("Showing commit history for " + user.github_username + " since " + startDateString)

  totalCommitCount = 0
  nonWorkdayCommitCount = 0
  for repo in gitUser.get_repos():
    reponame = repo.name
    if(repo.size == 0):
      #Repository is empty. Skip it to avoid a githubException (204 no content http response)
      continue

    commits = repo.get_commits(since=startDate, author=gitUser)
    if(commits.totalCount == 0 or commits[commits.totalCount-1].commit.author.date < startDate):
      #The user has not committed to the current repository in the given time period.
      continue
    else:
      print("Commits to " + reponame + ":")

      for commit in commits:
        timestamp = commit.commit.author.date
        output = str(timestamp)
        if timestamp.weekday()>5:
          output += " !Weekend!"
          nonWorkdayCommitCount += 1
        elif timestamp.hour < 7 or timestamp.hour >= 19:
          #Commit is after 7pm or early in the morning (could be an all-nighter)
          output += " !night!"
          nonWorkdayCommitCount += 1
        print(output)
        totalCommitCount += 1
  offHourCommitPercentage = nonWorkdayCommitCount * 100.0 / totalCommitCount
  print("Total commits: " + str(totalCommitCount))
  print("Off-hour commits: " + str(nonWorkdayCommitCount) + " (" + str(offHourCommitPercentage) + "%)")

  return

