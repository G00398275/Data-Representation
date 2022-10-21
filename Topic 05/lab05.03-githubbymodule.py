'''Lab 05.03 - pyGithub; Data Representation Winter 2022
This program uses the pyGithub package to interact with GitHub
Author: Ross Downey
Lecturer: Andrew Beatty'''

import requests
import json
from github import Github # pyGithub
from config import configGithub as cfg # API token from Github added to config.py file

apikey = cfg["githubkey"] # API key from config.py

g = Github(apikey) # applying variable to github api key

for repo in g.get_user().get_repos():
    print(repo.name) # Printing repository names

# Outputting a clone of the url of the github repo
repo = g.get_repo("G00398275/aprivateone")
#print(repo.clone_url) 

# Getting the url of the file in the github repo
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Calling the contents of the file in the github repo
response = requests.get(urlOfFile)
contentOfFile = response.text
# print (contentOfFile)

# Adding a line to the text file in github
newContents = contentOfFile + " more stuff 2\n"
# print (newContents)

# Updating the file, note syntax and fileinfo.sha
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
# print (gitHubResponse)


