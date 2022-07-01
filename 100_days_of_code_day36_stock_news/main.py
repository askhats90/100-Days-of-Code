import os
import requests
import math
import datetime as dt
import random

# Format the SMS/email message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

STOCK = 'TSLA'
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
ALPHA_VANTAGE_ENDPOINT = 'https://www.alphavantage.co/query'
ALPHA_VANTAGE_SERVICE = 'GLOBAL_QUOTE'
NEWS_API_API_KEY = os.getenv('NEWS_API_API_KEY')
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'

av_parameters = {
    "function": ALPHA_VANTAGE_SERVICE,
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

av_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=av_parameters)
av_response.raise_for_status()
av_data = av_response.json()

change_percent = av_data['Global Quote']['10. change percent'][:-1]
number_parts = change_percent.split('.')
number = int(''.join(number_parts))
change_percent = number / math.pow(10, len(number_parts[1]))

if round(change_percent) >= 2 or round(change_percent) <= -2:
    today = dt.datetime.today().date()
    three_days_ago = today - dt.timedelta(days=3)

    na_parameters = {
        'apiKey': NEWS_API_API_KEY,
        'q': COMPANY_NAME,
        'searchIn': 'title,description',
        'language': 'en',
        'from': str(three_days_ago),
        'to': str(today)
    }
    na_response = requests.get(url=NEWS_API_ENDPOINT, params=na_parameters)
    na_response.raise_for_status()
    na_data = na_response.json()

    titles = [x['title'] for x in na_data['articles']]
    descriptions = [y['description'] for y in na_data['articles']]

    if round(change_percent) >= 2:
        sign = f"🔺{round(change_percent)}%"
    else:
        sign = f"🔻{round(change_percent) * -1}%"

    random_number = random.randint(0, len(titles) - 1)
    message = f"{STOCK}: {sign}\nHeadline: {titles[random_number]}\nBrief: {descriptions[random_number]}"

    # We just print the message instead of sending via SMS or email
    print(message)
