import requests
import os
import datetime
from flight_data import FlightData

API_KEY = os.environ["API_KEY_FLIGHT"]
IATA_code_search_endpoint = "https://tequila-api.kiwi.com/locations/query"
flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
headers = {
    "apikey": API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, own_city):
        self.now = datetime.datetime.now()
        tmr = self.now + datetime.timedelta(days=1)
        six_month = self.now + datetime.timedelta(days=180)
        self.date_tmr = tmr.strftime("%d/%m/%Y")
        self.date_six_month = six_month.strftime("%d/%m/%Y")
        self.flight_data = FlightData()
        self.own_city = own_city

    def search_city(self, city):
        parameter = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(IATA_code_search_endpoint, parameter, headers=headers)
        response.raise_for_status()
        data = self.flight_data.check_city(response.json())
        return data

    def search_flight(self, city, lowest_price, stopover=0):
        parameter = {
            "curr": "GBP",
            "fly_from": self.own_city,
            "fly_to": city,
            "date_from": self.date_tmr,
            "date_to": self.date_six_month,
            "price_to": lowest_price,
            "sort": "price",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": stopover,
        }
        response = requests.get(flight_search_endpoint, parameter, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data["data"]:
            return self.flight_data.check_price(data, parameter["max_stopovers"])
        else:
            print(f"{parameter['max_stopovers']} no flight found")
            # print(data)
            if parameter["max_stopovers"] < 2:
                self.search_flight(city, lowest_price, parameter["max_stopovers"]+1)

        # print(response.json())



