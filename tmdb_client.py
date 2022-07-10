from flask import Flask
import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzVjYzBlZWYxNTg4OGM4YTRjNjI1ZjcwMjc4ZTlmMCIsInN1YiI6IjYyYzU4NzJiZThkMDI4MDBjOWFiM2MxNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vyREpDimE4jZ_ib1fRxB08D0cQlZI6Z5bPaRAa2vxlU"

app = Flask(__name__)
app.config["SECRET_KEY"] = 'alamakota'

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()
    
def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
         "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_urls(poster_api_path, size):
    tmdb_url = "https://image.tmdb.org/t/p/"
    poster_url = f"{tmdb_url}{size}{poster_api_path}"
    return poster_url

def get_movies(how_many, list_type='popular'):
    data = get_popular_movies()
    random.shuffle(data['results'])
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()["cast"]

def get_cast(movie_id, how_many=8):
    data = get_single_movie_cast(movie_id)
    return data[:how_many]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint_2 = endpoint + "?api_key=" + API_TOKEN
    response = requests.get(endpoint_2, headers=headers)
    return response.json()