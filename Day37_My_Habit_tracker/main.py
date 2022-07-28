import requests, datetime

TOKEN = "shaheen1994key"
USERNAME = "shaheen94"
GRAPHID = "graph94"
pixela_endpoint = "https://pixe.la//v1/users"
user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
pixela_graph_endpoint = "https://pixe.la//v1/users/shaheen94/graphs"

headers = {
   "X-USER-TOKEN":TOKEN
}

graph_params = {
    "id": GRAPHID,
    "name": "CodingPassion",
    "unit": "Hrs",
    "type": "int",
    "color": "ichou",
    "timezone": "UTC",
}
# response1 = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# print(response1.text)

pixela_pixel_endpoint = "https://pixe.la//v1/users/shaheen94/graphs/graph94"
# autofilling today's using strtime() method
today = datetime.datetime.now()
# print(today)

pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "5"
}
response = requests.post(url=pixela_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
















