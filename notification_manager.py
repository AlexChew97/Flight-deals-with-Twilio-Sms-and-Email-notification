import os
from twilio.rest import Client
import smtplib

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
email = os.environ["Email"]
password = os.environ["Password"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message_to_send):
        message = self.client.messages \
            .create(
            body=message_to_send,
            from_=os.environ["virtual_phone"],
            to=os.environ["my_phone"]
        )

        return message.status

    def send_email(self, message, google_flight_link, user_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(email, user_email, f"Subject:Cheap Flight!!!"
                                                                     f"\n\n{message.encode('UTF-8')}"
                                                                     f"\n{google_flight_link}")
