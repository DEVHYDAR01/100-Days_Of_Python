#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

ACCESS_TOKEN = ""

Auth_header = {
    "Authorization": ACCESS_TOKEN,
}

CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
SHETTY_GET_API_ENDPOINT = "https://api.sheety.co/22a43baf6879d0968bcba81323c2b3ca/copyOfFlightDeals/prices"

response = requests.get(url=SHETTY_GET_API_ENDPOINT)
shetty_data = response.json()["prices"]
city_names = [data["city"] for data in shetty_data]
iata_codes = []

for city in city_names:
    params = {
        "keyword": city,
        "max": "10"
    }
    response = requests.get(url=CITY_SEARCH_ENDPOINT, headers=Auth_header, params=params)
    response.raise_for_status()
    city_search_data = response.json()
    get_iata_code = city_search_data["data"][0]["iataCode"]
    print(get_iata_code)
    iata_codes.append(get_iata_code)
#
for idx, data in enumerate(shetty_data):
    object_id = data["id"]
    SHETTY_PUT_API_ENDPOINT = f"https://api.sheety.co/22a43baf6879d0968bcba81323c2b3ca/copyOfFlightDeals/prices/{object_id}"
    edit_payload = {
        "price": {
            "iataCode": iata_codes[idx],
            "content-Type": "application/json"
        }
    }
    put_response = requests.put(SHETTY_PUT_API_ENDPOINT, json=edit_payload)
    # put_response.raise_for_status()
    print(put_response.text)