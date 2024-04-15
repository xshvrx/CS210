 --- PART 1: READING DATA ---
import pandas as pd
import csv
# 1.1
def read_ratings_data(f):
    movie_ratings = {}
 
    with open(f, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            user_id = int(parts[0])
            movie_id = int(parts[1])
            rating = float(parts[2])
            if movie_id not in movie_ratings:
                movie_ratings[movie_id] = []
            movie_ratings[movie_id].append(rating)
 
    return movie_ratings
 
# 1.2
def read_movies_data(f):
    data = []
 
    with open(f, 'r') as file:
        for line in sorted(file.readlines(), key=lambda line: int(line.strip().split('|')[0])):
            parts = line.strip().split('|')
            if len(parts) == 4:
                data.append([int(parts[0]), parts[1], int(parts[2]), parts[3]])
    columns = ["movie_id", "title", "year", "genre"]
    df = pd.DataFrame(data, columns=columns).set_index("movie_id")
    
    return df
 
# --- PART 2: PROCESSING DATA ---
 
# 2.1
def get_movie(movies_df, movie_id):
    pass
 
# 2.2
def create_genre_dict(movies_df):
    genre_dict = {}
    for index, row in movies_df.iterrows():
        genres = row['genre'].split('|')
        for genre in genres:
            if genre in genre_dict:
                genre_dict[genre].append(index)
            else:
                genre_dict[genre] = [index]
    return genre_dict
 
# 2.3
def calculate_average_rating(ratings_dict, movies_df): 
    total_ratings = {}
    ratings_count = {}
 
    for movie_id, ratings in ratings_dict.items():
        total_ratings[movie_id] = sum(ratings)
        ratings_count[movie_id] = len(ratings)
    average_ratings = {}
    for movie_id in total_ratings.keys():
        if movie_id in ratings_count:
            average_ratings[movie_id] = total_ratings[movie_id] / ratings_count[movie_id]
    average_ratings_series = pd.Series(average_ratings)
    
    return average_ratings_series
 
# --- PART 3: RECOMMENDATION ---
 
# 3.1
def get_popular_movies(avg_ratings, n=10):
    sorted_ratings = avg_ratings.sort_values(ascending=False)
    top_movies = sorted_ratings.head(n)
    
    return top_movies
 
# 3.2
def filter_movies(avg_ratings, thres_rating=3):
    filtered_movies = avg_ratings[avg_ratings >= thres_rating]
    
    return filtered_movies
 
# 3.3
def get_popular_in_genre(genre, genre_to_movies, avg_ratings, n=5):
    movies_in_genre = genre_to_movies.get(genre, [])
    avg_ratings_in_genre = avg_ratings[movies_in_genre]
    top_movies = avg_ratings_in_genre.sort_values(ascending=False).head(n)
    
    return top_movies
 
# 3.4
def get_genre_rating(genre, genre_to_movies, avg_ratings):
    movies_in_genre = genre_to_movies.get(genre, [])
    avg_ratings_in_genre = avg_ratings[movies_in_genre]
    average_rating = avg_ratings_in_genre.mean()
    
    return average_rating
 
# 3.5
def get_movie_of_the_year(year, avg_ratings, movies_df):
    movies_in_year = movies_df[movies_df['year'] == year]
 
    if not movies_in_year.empty:
        highest_rated_movie_id = avg_ratings[movies_in_year.index].idxmax()
        highest_rated_movie_title = movies_df.loc[highest_rated_movie_id, 'title']
        return highest_rated_movie_title
    else:
        return None
 
 
 
# --- PART 4: USER FOCUSED ---
 
# 4.1
def read_user_ratings(f):
    user_movies = {}
 
    with open(f, 'r') as file:
        for line in file:
            user_id, movie_id, rating = line.strip().split(',')
            user_id = int(user_id)
            movie_id = int(movie_id)
            rating = float(rating)
            if user_id in user_movies:
                user_movies[user_id].append((movie_id, rating))
            else:
                user_movies[user_id] = [(movie_id, rating)]
 
    return user_movies
 
 
# 4.2
def get_user_genre(user_id, user_to_movies, movies_df):
    if user_id not in user_to_movies:
        return None
    
    genre_ratings = {}
    user_ratings = user_to_movies[user_id]
 
    for movie_id, rating in user_ratings:
        movie_genres = movies_df[movies_df.index == movie_id]['genre'].values[0].split('|')
        for genre in movie_genres:
            if genre in genre_ratings:
                genre_ratings[genre].append(rating)
            else:
                genre_ratings[genre] = [rating]
    genre_average_ratings = {genre: sum(ratings) / len(ratings) for genre, ratings in genre_ratings.items()}
    top_genre = max(genre_average_ratings, key=genre_average_ratings.get)
 
    return top_genre
 
# 4.3
def recommend_movies(user_id, user_to_movies, movies_df, avg_ratings):
    user_top_genre = get_user_genre(user_id, user_to_movies, movies_df)
 
    if user_top_genre is not None:
        top_genre_movies = movies_df[movies_df["genre"] == user_top_genre]
        rated_movies = [movie[0] for movie in user_to_movies[user_id]]
        unrated_movies = top_genre_movies.index.difference(rated_movies)
        avg_ratings_unrated = avg_ratings[unrated_movies]
        recommended_movies = avg_ratings_unrated.sort_values(ascending=False)
        return recommended_movies.head(3)
    else:
        return None
