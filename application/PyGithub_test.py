#Simple example which prints the names of all my git repos
from application import application
from application.models import GithubUser

from github import Github

#List all the repos for a given user (currently first authenticated one in the database)
def listRepos():
  # using an access token (TODO: grab by user or something)
  user = GithubUser.query.filter(GithubUser.github_oauth_access_token.isnot(None)).first()
  g = Github(user.github_oauth_access_token)

  # Github Enterprise with custom hostname
  #g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

  for repo in g.get_user().get_repos():
    print(repo.name)
    # to see all the available attributes and methods
    #print(dir(repo))
