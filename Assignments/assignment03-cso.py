# Data Representation - ATU Winter 2022
# Assignment 03 - CSO Data Import
# Author: Ross Downey
# Lecturer: Andrew Beatty

# Import required modules
from ast import Pass
import requests
import json

# url from CSO site, can insert the exact data required between beginning and end
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# Function for taking all data needed in json format and adding to file, not formatted correctly
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

# Function for getting all the data from CSO site, used in getAllAsFile above
def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    # Code FIQ02 is the exchequer account (historical series) on CSO site, used as dataset above
    getAllAsFile("FIQ02")
    