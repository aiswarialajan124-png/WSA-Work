from github import Github
from config import config as cfg

apikey = cfg["githubkey"]

g = Github(apikey)

for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("aiswarialajan124-png/aprivateone")
print(repo.clone_url)
