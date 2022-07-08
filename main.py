from flask import Flask, render_template, url_for
import tmdb_client
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    movies = tmdb_client.get_movies(how_many=12)
    return render_template("homepage.html", movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_poster_url(path, size):
        return tmdb_client.get_poster_urls(path, size)
    return {"tmdb_poster_url": tmdb_poster_url}

#@app.route("/movie/<movie_id>")
#def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=details)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)