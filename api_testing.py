# # url = "https://v1.american-football.api-sports.io/leagues"
#
# # api_key = '9fe360f84b458f8f87f7dbc6119a9323'
#
# # payload={}
# # headers = {
# #   'x-rapidapi-key': 'api_key',
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

from creds import sports_key
# headers = {
#     'x-rapidapi-host': "v1.american-football.api-sports.io",
# 'x-rapidapi-key': sports_key,
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
#     'x-rapidapi-key': sports_key,
#     'x-rapidapi-host': 'v1.american-football.api-sports.io'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# # print(response.text)
# pprint.pprint(requests.Request)

import http.client
import json

conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.american-football.api-sports.io",
    'x-rapidapi-key': sports_key
    }

conn.request("GET", "/teams?id=24", headers=headers)

res = conn.getresponse()
data = res.read()

pprint.pprint(json.loads(data.decode("utf-8")))