import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.tomorrow = datetime(year=2024, month=12, day=13)
        self.months_6 = self.tomorrow + timedelta(days=6 * 30)
        self._api_key = os.getenv("Amadeus_API_Key")
        self._api_secret = os.getenv("Amadeus_SECRET_Key")
        self.auth_token_header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self.auth_token_config_data = {
            "grant_type":  "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        self._token = self._get_new_token()
        self.auth_header = {
            "Authorization": self._token,
        }

    def _get_new_token(self):
        auth_response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token",
                                      data=self.auth_token_config_data, headers=self.auth_token_header)
        auth_response.raise_for_status()
        auth_response_data = auth_response.json()
        token_type = auth_response_data["token_type"]
        access_token = auth_response_data["access_token"]
        token = token_type + " " + access_token
        return token

    def get_iata_codes(self, city_name):
        params = {
            "keyword": city_name,
            "max": "10"
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
                                headers=self.auth_header, params=params)
        response.raise_for_status()
        city_search_data = response.json()
        get_iata_code = city_search_data["data"][0]["iataCode"]
        return get_iata_code

    def flight_search(self, city_code, is_direct=True):
        flight_params = {
            "originLocationCode": "LON",
            "destinationLocationCode": city_code,
            "departureDate": self.tomorrow.strftime("%Y-%m-%d"),
            "returnDate": self.months_6.strftime("%Y-%m-%d"),
            "max": 50,
            "nonStop": "true" if is_direct else "false",
            "adults": 1
        }

        response = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers",
                                headers=self.auth_header, params=flight_params)
        # response.raise_for_status()
        flight_data = response.json()

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        return flight_data




# curl "https://test.api.amadeus.com/v1/security/oauth2/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=kPtnnlGUMArJh0yFnuN9uNruTwnwJAVv&client_secret=mAcqXMooM1nSSVlL"
# Warning

