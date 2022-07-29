from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    year = IntegerField("Movie Year")
    description = StringField("Movie Description")
    img_url = StringField("Movie Poster URL")
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    for movie in all_movies:
        movie.ranking = len(all_movies) - all_movies.index(movie)
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    page = request.args.get('id', type=int)
    title = Movie.query.get(page).title
    if form.validate_on_submit():
        Movie.query.get(page).rating = float(form.rating.data)
        Movie.query.get(page).review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', title=title, form=form)


@app.route("/delete")
def delete():
    page = request.args.get('id', type=int)
    db.session.delete(Movie.query.get(page))
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            img_url=form.img_url.data)
        db.session.add(new_movie)
        db.session.commit()
        movie_id = Movie.query.filter_by(title=form.title.data).first().id
        return redirect(url_for('edit', id=movie_id))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
