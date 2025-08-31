# url = "https://v1.american-football.api-sports.io/leagues"
# from creds import api_key

# payload={}
# headers = {
#   'x-rapidapi-key': 'api_key',
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

# from pprint import pprint

import pprint

conn = http.client.HTTPSConnection("v1.american-football.api-sports.io")

from creds import api_key

headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io"
'x-rapidapi-key':'api_key',
"content-type": "application/json"
}

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))
pprint.pprint(data)

# url = "https://v1.american-football.api-sports.io/leagues"
#
# payload = {}
# headers = {
#     'x-rapidapi-key': 'api_key',
#     'x-rapidapi-host': 'v1.american-football.api-sports.io'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# # print(response.text)
# pprint.pprint(data)
