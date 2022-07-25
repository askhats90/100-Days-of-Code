from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from test import MyForm


def create_app():
    a = Flask(__name__)
    Bootstrap(a)
    a.secret_key = 'abcd'
    return a


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        return admin_cred(email=form.email.data, password=form.password.data)
    return render_template('login.html', form=form)


def admin_cred(email, password):
    if email == 'admin@email.com' and password == '12341234':
        return render_template('success.html')
    else:
        return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)