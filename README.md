# PopcornPick Backend – FastAPI Movie Recommender API

This is the backend service for **PopcornPick**, a movie recommendation web app. It uses **FastAPI** to serve a machine learning model trained on movie metadata to provide content-based recommendations.

---

## 🚀 Features

- 📦 RESTful API built with FastAPI
- 🧠 Content-based movie recommendation using cosine similarity
- 🗂 Pre-processed data stored as `.pkl` files (movie dictionary and similarity matrix)
- 🌐 CORS enabled for cross-origin frontend requests
- 🧾 JSON API responses for easy integration

---

## 📁 Project Structure

```

backend/
├── main.py                  # FastAPI app entry point
├── data/
│   ├── movie_dict.pkl       # Serialized movie data (title, id, etc.)
│   └── similarity.pkl       # Precomputed similarity matrix
├── requirements.txt         # Python dependencies

````

---

## 🧠 How It Works

1. **movie_dict.pkl** — A dictionary of movies (title, ID, etc.) converted to a DataFrame
2. **similarity.pkl** — A cosine similarity matrix between movies based on their metadata (genre, cast, keywords, etc.)
3. API receives a movie title and returns the top 5 most similar movies
4. Frontend then fetches poster data using TMDb API

---

## 🌐 API Endpoints

### `GET /`

Returns a welcome message

```json
{ "message": "Welcome to PopcornPick" }
```

---

### `GET /movies`

Returns a list of all movie titles

```json
["Inception", "Titanic", "Interstellar", ...]
```

---

### `GET /movies/{movie_name}`

Returns the top 5 similar movies for the selected movie

#### Example:

**Request:**
`GET /movies/Inception`

**Response:**

```json
[
  { "id": 27205, "title": "Interstellar" },
  { "id": 12345, "title": "The Matrix" },
  ...
]
```

---

## 🔐 CORS Configuration

CORS is configured to allow requests only from specified frontend origins:

```python
origins = os.getenv("FRONTEND_ORIGINS").split(",")
```

Set the environment variable in your host (or `.env` file):

```
FRONTEND_ORIGINS=https://popcornpickapp.netlify.app
```

---

## 🧪 Dependencies

```txt
fastapi
uvicorn
pandas
pickle
python-dotenv
```

---

## 📦 Exported Files (from Jupyter Notebook)

These files are **generated from your ML model** training in a separate notebook:

* `movie_dict.pkl`
* `similarity.pkl`

Make sure to place them inside the `/data` directory.

---



## 👨‍💻 Author

**Devansh Tyagi**
Full-Stack Developer & Machine Learning Enthusiast
📫 [LinkedIn](https://www.linkedin.com/in/devansh-tyagi/) | 🧠 [GitHub](https://github.com/devanshtyagi26)

---

## ⭐️ Support

If this backend helped you, give the full project a ⭐ and consider sharing!

