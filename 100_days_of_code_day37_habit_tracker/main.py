import requests
import datetime as dt
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
GRAPH_ID = "graph01"
day = dt.datetime.today() - dt.timedelta(0)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
UPDATE_GRAPH01_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{day.strftime('%Y%m%d')}"

headers = {
    'X-USER-TOKEN': TOKEN
}

# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
#
# new_user = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#
# graph_params = {
#     'id': 'graph01',
#     'name': 'graph01',
#     'unit': 'goals',
#     'type': 'int',
#     'color': 'ajisai',
#     'timezone': 'Asia/Almaty',
# }
#
# new_graph = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)

pixel_params = {
    'date': day.strftime("%Y%m%d"),
    'quantity': input("How many goals did I score? ")
}

new_pixel = requests.post(url=UPDATE_GRAPH01_ENDPOINT, json=pixel_params, headers=headers)
print(new_pixel.text)

# pixel_update_params = {
#     'quantity': '5'
# }
#
# pixel_update = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=pixel_update_params, headers=headers)

# pixel_delete = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
