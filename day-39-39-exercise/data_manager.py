import requests
from dotenv import load_dotenv
import os

load_dotenv()
class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def deliver_iatacodes(self, object_id, city):
        shetty_header = {
            "Authorization": os.getenv("AUTHORIZATION"),
            "Content-Type": "application/json"
        }

        shetty_put_config = {
            "price": {
                "iataCode": city,
            }
        }
        response = requests.put(os.getenv("sheet_put_endpoint"),
                                json=shetty_put_config, headers=shetty_header)
        # response.raise_for_status()
        print(response.json())

    def get_customer_emails(self):
        shetty_header = {
            "Authorization": os.getenv("AUTHORIZATION"),
            "Content-Type": "application/json"
        }
        response = requests.get(os.getenv("sheet_user_get_endpoint"), headers=shetty_header)
        response.raise_for_status()
        user_data = response.json()["users"]
        return user_data


data = DataManager()
customer_mails = data.get_customer_emails()
user_emails = [user_email["whatIsYourEmail?"] for user_email in customer_mails]
print(user_emails)

