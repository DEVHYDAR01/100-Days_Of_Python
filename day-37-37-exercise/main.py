import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = os.getenv("TOKEN")
print(TOKEN)
USERNAME = "hydar"

# pixela_params = {
#     "token": "sadasdsdasdasdfgd",
#     "username": "hydar",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
#     "thanksCode": "thanks-code"
# }
#
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_header = {
    "X-USER-TOKEN": TOKEN
}

# graph_config = {
#     "id": "graph1",
#     "name": "cycling graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai",
#
# }
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
# print(response.text)

# today = datetime(2024, 11, 28)

graph_post_endpoint = f"{graph_endpoint}/graph1"

# graph_post_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "9.5",
# }

# response = requests.post(url=graph_post_endpoint, json=graph_post_config, headers=graph_header)
# print(response.text)

graph_put_endpoint = f"{graph_post_endpoint}/20241128"

graph_put_config = {
    "quantity": "5.5",
}
#
# response = requests.put(url=graph_put_endpoint, json=graph_put_config, headers=graph_header)
# print(response.text)

# graph_delete_endpoint = graph_put_endpoint
#
# response = requests.delete(url=graph_delete_endpoint, headers=graph_header)
# print(response.text)
