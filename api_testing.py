# url = "https://v1.american-football.api-sports.io/leagues"
#
# payload={}
# headers = {
#   'x-rapidapi-key': '9fe360f84b458f8f87f7dbc6119a9323',
#   'x-rapidapi-host': 'v1.american-football.api-sports.io'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
#
#
#
#
#
#
#
#
# get("https://v1.american-football.api-sports.io/status");

import http.client
from pprint import pprint

import requests

conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.american-football.api-sports.io",
    'x-rapidapi-key': "9fe360f84b458f8f87f7dbc6119a9323"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


url = "https://v1.american-football.api-sports.io/leagues"

payload={}
headers = {
  'x-rapidapi-key': '9fe360f84b458f8f87f7dbc6119a9323',
  'x-rapidapi-host': 'v1.american-football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

pprint(response.text)