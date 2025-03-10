import pandas as pd

# Load dataset (Modify path based on dataset chosen)
ratings = pd.read_csv("data/ratings.csv")
movies = pd.read_csv("data/movies.csv")

# Display dataset information
print("Ratings Dataset:")
print(ratings.head())

print("\nMovies Dataset:")
print(movies.head())

# Based on the movieID column, merge the Movies and Ratings Dataset
data = pd.merge(ratings, movies, on="movieId")

# Display first few rows
print("\nMerged Data:")
print(data.head())

# Save the merged dataset to csv
data.to_csv("data/merged_ratings.csv", index=False)

# Exploratory Data Analysis (EDA)

