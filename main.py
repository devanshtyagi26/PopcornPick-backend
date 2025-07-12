from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  
from typing import List
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

# Load data
movies_dict = pickle.load(open('data/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

app = FastAPI()

# Load allowed origins from env var or fallback to default list
origins = os.getenv("FRONTEND_ORIGINS").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],  # only GET requests allowed
    allow_headers=["Authorization", "Content-Type", "Accept", "Origin", "User-Agent", "X-Requested-With"],
)


class Hero(BaseModel):
    id: int
    name: str
    origin: str

heroes: List[Hero] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to PopcornPick"}

@app.get("/movies")
def all_movies():
    return movies['title'].tolist()

@app.get("/movies/{movie}")
def get_movie(movie: str):
    if movie not in movies['title'].values:
        raise HTTPException(status_code=404, detail="Movie not found in dataset.")
    
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    output = []
    for i in movies_list:
        movie_id = int(movies.iloc[i[0]].movie_id)
        movie_title = movies.iloc[i[0]].title
        output.append({
            "id": movie_id,
            "title": movie_title
        })

    return output
