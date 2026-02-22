from github import Github, Auth
from config import config as cfg

# get api key
apikey = cfg["githubkey"]

# authenticate
auth = Auth.Token(apikey)
g = Github(auth=auth)

# get repository
repo = g.get_repo("aiswarialajan124-png/WSA-Work")

# get file from assignment folder
fileInfo = repo.get_contents("assignment/assignment04.txt")

# read content
content = fileInfo.decoded_content.decode("utf-8")

print("Original content:")
print(content)

# update content
updated_content = content.replace("Aiswaria", "Aiswaria Lajan")

print("Updated content")
print(updated_content)

# update file in github
repo.update_file(
    fileInfo.path,
    "Replaces Aiswaria with full name",
    updated_content,
    fileInfo.sha
)

print("Assignment updated successfully.")