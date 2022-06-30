import requests

parameters = {
    'lat': [your_latitude],
    'lon': [your_longitude],
    'appid': [your_appid],
    'units': 'metric',
}

weather_api = 'https://api.openweathermap.org/data/2.5/weather'
onecall_api = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(url=onecall_api, params=parameters)
response.raise_for_status()
data = response.json()

hourly = data['hourly']
hourly_temp_list = [{hourly.index(item): [item['temp'], item['weather'][0].get('id'), item['weather'][0].get('main')]} for item in hourly if hourly.index(item) < 12]

for i in hourly_temp_list:
    for j in i:
        if i[j][1] < 700:
            print(f"On day {j} expecting {i[j][2].lower()} - Bring an umbrella.")
