from importlib.metadata import packages_distributions
import requests
import pandas
import requests
import config

KEY = config.API_KEY


# function to retrieve the current most popular movies and their corresponding ID from the TMDB API
#   params:
#   - pages (int): number of pages of 20 movies to retrieve from the db
#   returns:
#   - df (pandas.DataFrame): DataFrame of the movies' title and ID
def get_popular_movies(pages):
    columns = ['film', 'id']
    df = pandas.DataFrame(columns=columns)

    for page in range(1, pages+1):
        response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={KEY}&language=en-US&page={page}")
        top_rated = response.json()
        top_rated_films = top_rated['results']
        for film in top_rated_films:
            df.loc[len(df)]=[film['title'], film['id']]
    
    return df


# function to search the TMDB API using a movie title
#   params:
#   - title (string): the desired movie title
#   returns:
#   - df (pandas.DataFrame): DataFrame of the titles and IDs returned from the search
def search_movies(title):
    search_term = title.replace(' ', '-')

    columns = ['film', 'id']
    df = pandas.DataFrame(columns=columns)

    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={KEY}&language=en-US&query={search_term}&page=1&include_adult=false")
    results = response.json()
    results_f = results['results']
    for film in results_f:
        df.loc[len(df)]=[film['title'], film['id']]

    return df
