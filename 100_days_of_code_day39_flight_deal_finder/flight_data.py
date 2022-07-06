import requests
import os

ENDPOINT = os.environ.get('KIWI_ENDPOINT')
API_KEY = os.environ.get('KIWI_API_KEY')
HEADER = {'apikey': API_KEY}


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.city_codes = []

    def get_city_code(self, city):
        query = {'term': city}
        response = requests.get(url=ENDPOINT, params=query, headers=HEADER).json()
        city_code = response['locations'][0]['code']
        self.city_codes.append(city_code)
        return city_code
