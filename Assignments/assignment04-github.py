'''Assigment 04; Data Representation Winter 2022
This program reads a file from a repo, replaces all instances of  the word "Andrew" with "Ross"
Author: Ross Downey
Lecturer: Andrew Beatty'''

import requests
from github import Github # pyGithub
from config import configGithub as cfg # API token from Github added to config.py file

apikey = cfg["githubkey"]

g = Github(apikey)

# Outputting a clone of the url of the github repo
repo = g.get_repo("G00398275/aprivateone")
#print(repo.clone_url)  Testing

# Getting the url of the file in the github repo
fileInfo = repo.get_contents("assignment04_test.txt")
urlOfFile = fileInfo.download_url
# print (urlOfFile) Testing

# Calling the contents of the file in the github repo
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

# Using replace function to replace string "Andrew" with "Ross"
newContents = contentOfFile.replace("Andrew", "Ross")
print (newContents)

# Updating the file and committing
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)


