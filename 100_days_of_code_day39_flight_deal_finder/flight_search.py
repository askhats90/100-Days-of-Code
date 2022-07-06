import requests
import datetime as dt
import os

DEPARTURE_CITY_CODE = input("What city are you departing from? ").upper()
ENDPOINT = os.environ.get('KIWI_SEARCH_ENDPOINT')
API_KEY = os.environ.get('KIWI_API_KEY')
HEADER = {'apikey': API_KEY}
TODAY = dt.datetime.today().strftime("%d/%m/%Y")
AFTER_SIX_MONTHS = (dt.datetime.today() + dt.timedelta(int(input("Please specify how many days use in search? ")))).strftime("%d/%m/%Y")

params = {
    'fly_from': DEPARTURE_CITY_CODE,
    'fly_to': '',
    'date_from': TODAY,
    'date_to': AFTER_SIX_MONTHS,
    'one_for_city': 0,
    'max_stopovers': 0,
    'selected_cabins': 'M',
    'sort': 'price',
    'limit': 3
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_found_prices = {}

    def search_prices(self, city_code):
        params.pop('fly_to')
        params.update({'fly_to': city_code})
        response = requests.get(url=ENDPOINT, params=params, headers=HEADER).json()
        found_prices = []
        for x in range(params['limit']):
            date_price_pair = {}
            date_price_pair.update({dt.datetime.strptime(response['data'][x]['route'][0]['local_departure'],
                                                         '%Y-%m-%dT%H:%M:%S.%fz').strftime("%d/%m/%Y - %H:%M:%S"): response['data'][x]['price']})
            found_prices.append(date_price_pair)
        self.city_found_prices.update({city_code: found_prices})
        return self.city_found_prices
