from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form['book_name'],
                        author=request.form['book_author'],
                        rating=request.form['book_rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit_rating():
    if request.method == 'POST':
        page_post = request.args.get('id_post', type=int)
        Book.query.get(page_post).rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        page_get = request.args.get('id_get', type=int)
        book_name = Book.query.get(page_get).title
        book_rating = Book.query.get(page_get).rating
        return render_template('edit_rating.html', book_id=page_get, book_name=book_name, book_rating=book_rating)


@app.route("/delete")
def delete():
    page = request.args.get('id', type=int)
    db.session.delete(Book.query.get(page))
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
