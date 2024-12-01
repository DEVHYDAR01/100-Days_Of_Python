import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
Authorization_Header = {
    "Authorization": os.getenv("Authorization")
}

basic = HTTPBasicAuth(os.getenv("USERNAME"), os.getenv("PASSWORD"))
response = requests.get("https://api.sheety.co/22a43baf6879d0968bcba81323c2b3ca/workoutTracking/workouts", auth=basic,
                        headers=Authorization_Header)

NLP_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_endpoint = "https://api.sheety.co/22a43baf6879d0968bcba81323c2b3ca/workoutTracking/workouts"

NLP_config = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

NLP_parameters = {
    "query": input("Tell which exercise you did: "),
}

response = requests.post(url=NLP_endpoint, json=NLP_parameters, headers=NLP_config)
response.raise_for_status()
exercise_data = response.json()
print(exercise_data["exercises"])
for exercise in exercise_data["exercises"]:
    get_exercise = exercise["name"].title()
    get_duration = exercise["duration_min"]
    get_calories = exercise["nf_calories"]

    today = datetime.now()
    shetty_config = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": get_exercise,
            "duration": get_duration,
            "calories": get_calories,
            "content-Type": "application/json"
        }
    }
    response = requests.post(url=shetty_endpoint, json=shetty_config, headers=Authorization_Header)
    response.raise_for_status()
    print(response.text)

