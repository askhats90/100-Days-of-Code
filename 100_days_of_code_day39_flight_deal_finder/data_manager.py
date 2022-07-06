import requests
import os

ENDPOINT = os.environ.get('SHEETY_ENDPOINT')


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(url=ENDPOINT).json()['prices']
        self.new_row = {}

    def get_city(self, row_id):
        city = self.response[row_id - 2]['city']
        return city

    def get_price(self, row_id):
        price = self.response[row_id - 2]['lowestPrice']
        return price

    def fill_new_row(self, row_id, city_code):
        self.new_row.update({'city': self.get_city(row_id)})
        self.new_row.update({'iataCode': city_code})
        self.new_row.update({'lowestPrice': self.get_price(row_id)})

    def put_new_row(self, row_id):
        data = {'price': self.new_row}
        endpoint = f"{ENDPOINT}/{row_id}"
        inserted = requests.put(url=endpoint, json=data)
