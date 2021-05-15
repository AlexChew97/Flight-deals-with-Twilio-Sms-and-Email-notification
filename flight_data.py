class FlightData:
    # This class is responsible for structuring the flight data.
    def check_city(self, response):
        return response["locations"][0]["code"]

    def check_price(self, response, stop_over):
        data = response["data"]
        if data:
            minimum = data[0]
            price = minimum["price"]
            city_from = minimum["cityFrom"]
            fly_from = minimum["flyFrom"]
            city_to = minimum["cityTo"]
            fly_to = minimum["flyTo"]
            time_from = minimum["route"][0]["local_departure"][:10]
            time_to = minimum["route"][-1]["local_departure"][:10]
            if stop_over == 0:
                message = f"Low price alert! Only £{price} to fly from {city_from}-{fly_from} to {city_to}-{fly_to}, from " \
                          f"{time_from} to {time_to}."
            else:
                via_city = minimum["route"][1]["cityFrom"]
                if minimum["route"][-2]["cityTo"] != via_city:
                    via_city += f", {minimum['route'][-2]['cityTo']}"
                message = f"Low price alert! Only £{price} to fly from {city_from}-{fly_from} to {city_to}-{fly_to}, from " \
                          f"{time_from} to {time_to}.\n\nFlight has {stop_over} stop over, via {via_city}"
            google_flight_link = f"https://www.google.co.uk/flights?hl=en#flt={fly_from}.{fly_to}.{time_from}*" \
                                 f"{fly_to}.{fly_from}.{time_to}"
            return_value = (message, google_flight_link)
            return return_value
            # print(message)
