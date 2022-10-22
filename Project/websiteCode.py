import requests

url = "https://nfl-team-stats1.p.rapidapi.com/v1/nfl/teamStats"

querystring = {"year":"2021"}

headers = {
	"X-RapidAPI-Key": "f7a8632468msh27334ff8601836ep126b12jsnec3a9252146f",
	"X-RapidAPI-Host": "nfl-team-stats1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)