import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

TRACK_HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    # 'x-remote-user-id': '0',
    # 'Content-Type': 'json'
}

SHEETY_HEADERS = {
    'Authorization': f"Bearer {os.environ.get('TOKEN')}"
}

TRACK_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

query = {
 "query": input("What exercise did you do? "),
 "gender": "male",
 "weight_kg": 93.5,
 "height_cm": 175,
 "age": 32
}

response = requests.post(url=TRACK_ENDPOINT, json=query, headers=TRACK_HEADERS)
exercise_data = response.json()['exercises']

# spreadsheet = requests.get(url=SHEETY_ENDPOINT)
# spreadsheet.raise_for_status()
# workouts = spreadsheet.json()['workouts']

today = dt.datetime.today()

for exercise in exercise_data:
    new_workout = {
        'workout': {
            'date': today.strftime("%d/%m/%Y"),
            'time': today.strftime("%H:%M:%S"),
            'exercise': exercise['name'].title(),
            'duration': round(exercise['duration_min']),
            'calories': round(exercise['nf_calories']),
        }
    }

    new_row = requests.post(url=SHEETY_ENDPOINT, json=new_workout, headers=SHEETY_HEADERS)
    print(new_row.text)
