import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "someone@somewhere.com"
MY_PASSWORD = "123456"
now = dt.datetime.now()

birthday_data = pd.read_csv('birthdays.csv')
name = birthday_data.name[birthday_data.month == now.month][birthday_data.day == now.day].to_string(index=False)
email = birthday_data.email[birthday_data.month == now.month][birthday_data.day == now.day].to_string(index=False)

letters = []
for i in range(1, 4):
    with open(f'letter_templates/letter_{i}.txt') as letter:
        text = letter.read()
    letters.append(text)

random_letter = random.choice(letters)
random_letter_corrected = random_letter.replace('[NAME]', name)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{random_letter_corrected}"
                        )
