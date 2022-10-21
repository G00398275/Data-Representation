'''Lab 06.02 - API Keys; Data Representation Winter 2022
This program takes data from a private github repo using API key
Author: Ross Downey
Lecturer: Andrew Beatty'''

import requests
import json
from config import configGithub as cfg

filename = "private.json"

url = 'https://api.github.com/repos/G00398275/aprivateone'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)