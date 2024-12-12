#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from dotenv import load_dotenv
from pprint import pprint
import time
from datetime import datetime, timedelta

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

load_dotenv()
flight = FlightSearch()
data = DataManager()
notice_manager = NotificationManager()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = "LON"

shetty_header = {
    "Authorization": os.getenv("AUTHORIZATION"),
    "Content-Type": "application/json"
}
SHETTY_API_GET_ENDPOINT = "https://api.sheety.co/e47767fdbdc9a1c3817e4ec37aaa65fe/copyOfCopyOfCopyOfFlightDeals/prices"
shetty_response = requests.get(url=SHETTY_API_GET_ENDPOINT, headers=shetty_header)
shetty_response.raise_for_status()
sheet_data = shetty_response.json()["prices"]
pprint(sheet_data)

for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight.get_iata_codes(city["city"])
        data.deliver_iatacodes(city["id"], city["iataCode"])

# flight_search = flight.flight_search("PAR")
# print(flight_search)
# print(len(flight_search["data"][0]["itineraries"][0]["segments"]))
# data_flight.find_cheapest_flight(flight_search, "PARIS")
# to_email = "autobirthdaywisherinfo@gmail.com"

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight.flight_search(destination['iataCode'])
    # flight_data_price = float(flights["data"][0]["price"]["grandTotal"])
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight.flight_search(
            destination["iataCode"],
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        customer_mails = data.get_customer_emails()
        user_emails = [user_email["whatIsYourEmail?"] for user_email in customer_mails]
        for mail in user_emails:
            notice_manager.notifier(
                msg=f"Subject:Low price alert!\n\n Only £{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport},\n on {cheapest_flight.out_date} until {cheapest_flight.return_date}.".encode('utf-8'),
                to_mail=mail
            )
            print("sent....!!")








