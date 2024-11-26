import requests
from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv()

END_POINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

parameters = {
    "lat": "-1.832720",
    "lon": "109.967987",
    "exclude": "current,daily",
    "appid": API_KEY
}
# "lat": "10.545410",
# "lon": "7.435220",

response = requests.get(END_POINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hours_list = weather_data["hourly"][0:12]
list_of_id = [hours["weather"][0]["id"] for hours in hours_list]
will_rain = False
for code in list_of_id:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="it's going to rain today, remember to bring an ☂️",
        from_='+12242231211',
        to='+2349016092616'
    )

    print(message.status)



