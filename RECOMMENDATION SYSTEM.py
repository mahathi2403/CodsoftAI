import pandas as pd

# Sample user-movie ratings data
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
    'movie': ['Inception', 'Titanic', 'Avatar', 'Inception', 'Avatar', 'Titanic', 'Avatar', 'Inception'],
    'rating': [5, 4, 5, 4, 4, 5, 3, 2]
}

df = pd.DataFrame(data)

user_movie_matrix = df.pivot_table(index='user_id', columns='movie', values='rating')
print(user_movie_matrix)

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Fill missing values with 0
user_movie_matrix_filled = user_movie_matrix.fillna(0)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix_filled)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def recommend_movies(user_id, num_recommendations=2):
    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:]
    top_user = similar_users.index[0]

    # Movies rated by the most similar user but not by the target user
    user_movies = set(user_movie_matrix.loc[user_id].dropna().index)
    top_user_movies = set(user_movie_matrix.loc[top_user].dropna().index)
    recommendations = list(top_user_movies - user_movies)

    return recommendations[:num_recommendations]

# Example: Recommend movies for user 4
print("Recommendations for User 4:", recommend_movies(4))








