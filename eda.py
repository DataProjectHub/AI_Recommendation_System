import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged dataset
data = pd.read_csv("data/merged_ratings.csv")

# Check dataset information
print(data.info())

# Display the most rated movies
most_rated = data.groupby("title").size().sort_values(ascending=False)[:10]
print("\nMost Rated Movies:")
print(most_rated)

# Plot most rated movies
plt.figure(figsize=(12, 6))
most_rated.plot(kind="bar")
plt.xlabel("Movies")
plt.ylabel("Number of Ratings")
plt.title("Top 10 Most Rated Movies")
plt.xticks(rotation=45)
plt.show()
