from importlib.metadata import packages_distributions
import requests
import pandas
import requests
import config

KEY = config.API_KEY

pages_to_retrieve = 10

columns = ['film', 'poster']
df = pandas.DataFrame(columns=columns)

for page in range(1, pages_to_retrieve+1):
    response = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?api_key={KEY}&language=en-US&page={page}")

    top_rated = response.json()

    top_rated_films = top_rated['results']

    for film in top_rated_films:
        df.loc[len(df)]=[film['title'], f'<img src="https://image.tmdb.org/t/p/w500/{film["poster_path"]}">']

print(df)

df.to_csv('movies_from_tmdb.csv')