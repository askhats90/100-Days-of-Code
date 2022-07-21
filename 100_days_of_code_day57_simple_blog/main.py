from flask import Flask, render_template
import requests


def get_data():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return all_posts


app = Flask(__name__)


@app.route('/blog')
def home():
    all_posts = get_data()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def post(num):
    all_posts = get_data()
    return render_template("post.html", post=all_posts[num - 1])


if __name__ == "__main__":
    app.run(debug=True)
