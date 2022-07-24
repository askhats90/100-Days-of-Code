from flask import Flask, render_template, request
import requests
import datetime as dt
import smtplib
import os

MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=["someone@email.com"],
                            msg=f"Subject:Some message from blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
                            )


def get_data():
    response = requests.get(url='https://api.npoint.io/9284ebc538c5fe49304c')
    data = response.json()
    return data


app = Flask(__name__)


@app.route("/")
def homepage():
    data = get_data()
    date = dt.datetime.now()
    return render_template("index.html", posts=data, date=date)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        title = "Successfully sent your message"
        data = request.form
        print(data['username'])
        print(data['email'])
        print(data['phone'])
        print(data['message'])
        send_email(name=data['username'], email=data['email'], phone=data['phone'], message=data['message'])
        return render_template('contact.html', title=title)
    else:
        title = "Contact Me"
        return render_template("contact.html", title=title)


@app.route("/posts/<int:num>")
def get_post(num):
    data = get_data()
    date = dt.datetime.now()
    return render_template("post.html", post=data[num - 1], date=date)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
