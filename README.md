# Building a Movie Recommendation System

## Introduction

During my internship, I worked on developing a **Movie Recommendation System** using **collaborative filtering techniques with Singular Value Decomposition (SVD)**. The goal was to build a system that suggests movies based on user preferences. The dataset used was **MovieLens 100K**, which contains user ratings for various movies.

Throughout this journey, I faced multiple challenges, including **package compatibility issues, dependency errors, and computational limitations**. This blog-style README outlines how I tackled each issue and completed the project step by step.

## Step 1: Setting Up the Environment

To ensure an organized workspace, I created a dedicated project folder:

C:\Users\Dell\Desktop\CODSOFT_Recommendation_System

Inside this folder, I set up a virtual environment to manage dependencies efficiently:

python -m venv venv
venv\Scripts\activate

Installed the required Python libraries:
pip install pandas numpy matplotlib seaborn scikit-learn surprise flask

## Step 2: Downloading and Loading the MovieLens Dataset

1. **MovieLens 100K dataset**, which contains:
- **ratings.csv** – User ratings for movies
- **movies.csv** – Movie titles and genres

2. After downloading and extracting the dataset,loaded it into a Pandas DataFrame:

ratings = pd.read_csv("data/ratings.csv")
movies = pd.read_csv("data/movies.csv")

3. Merged the datasets ensured we had complete information:

data = pd.merge(ratings, movies, on="movieId")
data.to_csv("data/merged_ratings.csv", index=False)

## Step 3: Challenge 1 – `scikit-surprise` Installation Issue
I encountered the following error:

Microsoft Visual C++ 14.0 or greater is required. So I installed **Microsoft C++ Build Tools** from [Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and restarted my system. Then, I reinstalled the package:
pip install scikit-surprise

## Step 4: Implementing the SVD Model

Implemented **Singular Value Decomposition (SVD)** for collaborative filtering:

## Step 5: Challenge 2– NumPy 2.x Compatibility Issue

I encountered the following error:

A module that was compiled using NumPy 1.x cannot be run in NumPy 2.2.3. So resolved it by downgrading NumPy
pip uninstall numpy
pip install numpy<2

## Step 6: Generating Movie Recommendations

Implemented a function to recommend movies based on predicted ratings:

def get_recommendations(user_id, model, movies, num_recommendations=5):
    movie_ids = movies['movieId'].unique()
    predictions = [model.predict(user_id, movie_id) for movie_id in movie_ids]
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    top_movies = [movies[movies['movieId'] == pred.iid]['title'].values[0] for pred in predictions[:num_recommendations]]
    return top_movies


Calling this function with a sample user ID:

user_id = 1
recommended_movies = get_recommendations(user_id, model, movies)
print(f"Recommended Movies for User {user_id}: {recommended_movies}")

This successfully generated **personalized recommendations** for a given user.

## Step 7: Deploying the Model with Flask

To make the recommendation system accessible as an API, I built a Flask application:

from flask import Flask, request, jsonify
from collaborative_filtering import model, get_recommendations
import pandas as pd

movies = pd.read_csv("data/movies.csv")
app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    user_id = int(request.args.get("user_id"))
    recommendations = get_recommendations(user_id, model, movies)
    return jsonify({"User ID": user_id, "Recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)

python flask_app.py

By accessing /127.0.0.1:5000/recommend?user_id=1, returns JSON recommendations for the user.

## Step 8: Deploying on Render

Since deploying on a personal laptop is not ideal, I hosted the Flask API on **Render**. Steps:

1. **Create a GitHub Repository**

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/repo.git
git push -u origin main

2. **Deploy on Render**
- Go to [Render](https://render.com/)
- Create a new **Web Service**
- Connect it to the GitHub repository
- Set the **Start Command**: `gunicorn app:app`
- Deploy

## Conclusion

This project was a great learning experience. Some key takeaways:
- **Handling dependencies**: Fixing NumPy and Visual C++ build issues.
- **Understanding recommendation models**: Implementing SVD-based collaborative filtering.
- **Building a Flask API** for easy deployment.
- **Deploying on the cloud** using Render.

The final system provides **personalized movie recommendations** and is accessible via an API. This experience improved my problem-solving skills and deepened my understanding of recommendation systems.

