from github import Github, Auth
from config import config as cfg
import requests

apikey = cfg["githubkey"]

auth = Auth.Token(apikey)
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("aiswarialajan124-png/aprivateone")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
print(fileInfo.download_url)

response = requests.get(fileInfo.download_url)
contentOfFile = response.text
print(contentOfFile)
