from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

send_message = NotificationManager()
flight = FlightSearch("LON")

sheety_data = DataManager()
user_data = sheety_data.get_user_email()

for city in sheety_data.data:
    # get IATA code
    iata_code = flight.search_city(city["city"])
    lowest_price = city["lowestPrice"]
    # put IATA code to sheety
    if city["iataCode"] == "":
        sheety_data.put_data(iata_code, city["id"])
    # search lowest price
    for user in user_data:
        email_content = flight.search_flight(iata_code, lowest_price)
        if email_content:
            send_message.send_email(email_content[0], email_content[1], user["email"])

# for testing
# print(flight.search_city("Paris"))
# flight.search_flight("KUL", 414)

# input user info
# print("Welcome to Blaze's Flight Club.\nWe find the best flight deals and email you.")
# first = input("What is your first name?\n")
# last = input("What is your last name?\n")
# email = input("What is your email?\n")
# email_check = input("Type your email again.\n")
# if email == email_check:
#     sheety_user_data.post_user(first, last, email)
#     print("You're in the club!")
# else:
#     print("Please check your email is the same one.")
