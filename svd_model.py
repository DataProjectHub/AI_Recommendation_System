import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load dataset
ratings = pd.read_csv("data/ratings.csv")
movies = pd.read_csv("data/movies.csv")  

# Define reader and load dataset into Surprise format
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Split into train-test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Train the SVD model
model = SVD()
model.fit(trainset)

# Predict and evaluate
predictions = model.test(testset)
rmse = accuracy.rmse(predictions)
print(f"RMSE: {rmse}")

def get_recommendations(user_id, model, movies, num_recommendations=5):
    movie_ids = movies['movieId'].unique()
    predictions = [model.predict(user_id, movie_id) for movie_id in movie_ids]
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    top_movies = [movies[movies['movieId'] == pred.iid]['title'].values[0] for pred in predictions[:num_recommendations]]
    return top_movies

user_id = 1  # Change to any user ID
recommended_movies = get_recommendations(user_id, model, movies)
print(f"Recommended Movies for User {user_id}: {recommended_movies}")

