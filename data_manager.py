import requests
import os

sheety_endpoint = os.environ["sheety_endpoint"]
sheety_user_endpoint = os.environ["sheety_user_endpoint"]
headers = {
    "Authorization": os.environ["sheety_token"]
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(sheety_endpoint, headers=headers)
        response.raise_for_status()
        self.data = response.json()["prices"]

    def put_data(self, code, id):
        parameter = {
            "price": {
                "iataCode": code,
            }
        }
        requests.put(url=f"{sheety_endpoint}/{id}", json=parameter, headers=headers)

    def post_user(self, first, last, email):
        parameter = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email,
            }
        }
        requests.post(sheety_user_endpoint, json=parameter, headers=headers)

    def get_user_email(self):
        response = requests.get(sheety_user_endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["users"]
