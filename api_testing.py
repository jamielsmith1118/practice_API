from data import *

# # url = "https://v1.american-football.api-sports.io/leagues"
#
#
# # payload={}
# # headers = {
# #   'x-rapidapi-key': 'nfl_key',
# #   'x-rapidapi-host': 'v1.american-football.api-sports.io'
# # }
# #
# # response = requests.request("GET", url, headers=headers, data=payload)
# #
# # print(response.text)
# #
# #
# #
# #
# #
# #
# #
# #
# # get("https://v1.american-football.api-sports.io/status");
#
# import http.client
#
#
# import pprint
#
# conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")
#
import pprint

from creds import nfl_key
# headers = {
#     'x-rapidapi-host': "v1.american-football.api-sports.io",
# 'x-rapidapi-key': nfl_key,
# 'content-type': 'application/json'
# }
#
# conn.request("GET", "/leagues", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# # print(data.decode("utf-8"))
# pprint.pprint(data)
#
# import requests
#
# url = "https://v1.american-football.api-sports.io/leagues"
#
# payload = {}
# headers = {
#     'x-rapidapi-key': nfl_key,
#     'x-rapidapi-host': 'v1.american-football.api-sports.io'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# # print(response.text)
# pprint.pprint(requests.Request)








# # Team information
# import http.client
# import json
#
# conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")
#
# headers = {
#     'x-rapidapi-host': "v1.american-football.api-sports.io",
#     'x-rapidapi-key': nfl_key
#     }
#
# conn.request("GET", "/teams?id=29", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# pprint.pprint(json.loads(data.decode("utf-8")))

# pprint.pprint(my_team_data)

# # League Information
# import http.client
#
# conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")
#
# headers = {
#     'x-rapidapi-host': "v1.american-football.api-sports.io",
#     'x-rapidapi-key': nfl_key
#     }
#
# conn.request("GET", "/leagues", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# pprint.pprint(json.loads(data.decode("utf-8")))

# pprint.pprint(my_league_data['response'][0]['league']['name'])

for league in my_league_data['response']:
    print(league['league']['name'])

