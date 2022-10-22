

import requests
import json

url = "https://nfl-team-stats1.p.rapidapi.com/v1/nfl/teamStats"

yearOfStats = {"year":"2021"}

headers = {
	"X-RapidAPI-Key": "f7a8632468msh27334ff8601836ep126b12jsnec3a9252146f",
	"X-RapidAPI-Host": "nfl-team-stats1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=yearOfStats)

def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("nflStats.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)