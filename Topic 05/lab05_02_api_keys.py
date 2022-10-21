'''Lab 06.02 - API Keys; Data Representation Winter 2022
This program converts a wikipedia page to a pdf file
Author: Ross Downey
Lecturer: Andrew Beatty'''

import requests
import urllib.parse
from config import config as cfg # necessary libraries and api key from confi

targetUrl = "https://en.wikipedia.org"

apiKey = cfg["htmltopdfkey"] # From config.py file

apiurl = 'https://api.html2pdf.app/v1/generate'# Created API key on this site

params = {'url': targetUrl, 'apiKey': apiKey} # Parameters needed, url and key
parsedParams = urllib.parse.urlencode(params) # Parse the parameters
requestUrl = apiurl + "?" + parsedParams # Joinin the api site to the parameters

response = requests.get(requestUrl)
print (response.status_code) # Status code to check if successful or not

result = response.content # All content from wikipedia

with open ("document.pdf", "wb") as handler: # Create new file to add wiki content as pdf
    handler.write(result)