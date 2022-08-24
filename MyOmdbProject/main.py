
from flask import Flask, render_template, redirect, url_for, request
import requests
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
API_KEY = "b582cbe3"
OMDB_ENDPOINT = f"http://www.omdbapi.com/?apikey={API_KEY}"
# param = {
#     "s" : "Fast & Furious",
# }
# response = requests.get(url=omdb_endpoint, params=param)
# result = response.json()
# pprint(result)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_movies.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=True)
db.create_all()

# new_movie = Movie(
#      title="King Kong",
#      year=2010,
#      rating=5.6,
#  )
# db.session.add(new_movie)
# db.session.commit()
all_movies = []
@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html",movies=all_movies)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        submit_data = request.form
        print(submit_data)
        movie_title = request.form.get("moviename")
        print(movie_title)
        response = requests.get(OMDB_ENDPOINT, params={"s": movie_title})
        data = response.json()["Search"]
        return render_template("select.html", options=data)
    # if request.method == 'POST':
    #     new_movie = Movie(
    #     movie_title = request.form.get("moviename"),
    #     author = request.form.get(""),
    #     rating = request.form.get("rating"),
    #     )
    #     db.session.add(new_movie)
    #     db.session.commit()
    #     return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/find")
def find_movie():
    myimdb_id = request.args.get('id')
    print(myimdb_id)
    response = requests.get(OMDB_ENDPOINT, params={"i": myimdb_id})
    data = response.json()
    pprint(data)
    t = data['Title']
    print(t)
    new_movie = Movie(
        title=data['Title'],
        year=data['Year'],
        rating=data['imdbRating']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
