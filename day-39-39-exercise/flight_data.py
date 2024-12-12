class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(flight_search):
    if flight_search is None or not flight_search['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    flight_data_nr_stops = len(flight_search["data"][0]["itineraries"][0]["segments"]) - 1
    flight_data_origin_airport = flight_search["data"][0]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    flight_data_destination_airport = flight_search["data"][0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    flight_data_out_date = flight_search["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"]
    flight_data_return_date = flight_search["data"][0]["itineraries"][0]["segments"][0]["arrival"]["at"]
    flight_data_price = float(flight_search["data"][0]["price"]["grandTotal"])

    cheapest_flight = FlightData(flight_data_price, flight_data_origin_airport, flight_data_destination_airport,
                                 flight_data_out_date, flight_data_return_date, flight_data_nr_stops)

    for flight in flight_search["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < flight_data_price:
            lowest_price = price
            flight_data_origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            flight_data_destination_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            flight_data_out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            flight_data_return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, flight_data_origin_airport, flight_data_destination_airport,
                                         flight_data_out_date, flight_data_return_date)
            print(f"Lowest price to {flight_data_destination_airport} is £{lowest_price}")

    return cheapest_flight
