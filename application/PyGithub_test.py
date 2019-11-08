from github import Github

# using username and password
#g = Github("Callum-Mitchell", "puffball456")

# or using an access token
g = Github("ae3c966eeb6b92f7c0033eb339da164f66b55358")
# Token is for user Callum-Mitchell to access repos and user information

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

for repo in g.get_user().get_repos():
    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
