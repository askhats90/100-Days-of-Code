import json
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

fd = FlightData()
dm = DataManager()
fs = FlightSearch()

for i in range(2, 8):
    city = dm.get_city(i)
    city_code = fd.get_city_code(city)
    city_found_prices = fs.search_prices(city_code)
    dm.fill_new_row(i, city_code)
    dm.put_new_row(i)

# print(fs.city_found_prices)

with open('prices_info.json', 'w') as data_file:
    json.dump(fs.city_found_prices, data_file, indent=4)
