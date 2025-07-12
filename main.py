from fastapi import FastAPI
from pydantic import BaseModel  
from typing import List
import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict= pickle.load(open('data/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

app = FastAPI()

# Allow requests from your frontend origin(s)
origins = [
    "http://localhost:3000",  # your Next.js frontend during development
    # You can add your production frontend domain here too, e.g. "https://yourdomain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allow these origins
    allow_credentials=True,
    allow_methods=["*"],          # allow all HTTP methods (GET, POST, etc)
    allow_headers=["*"],          # allow all headers
)

class hero(BaseModel):
    id: int
    name: str
    origin: str

heroes: List[hero] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to PopcornPick"}

@app.get("/movies")
def all_movies():
    return movies['title'].tolist()

@app.get("/movies/{movie}")
def get_movie(movie: str):
    return recommend(movie)