import requests
import pandas
import requests

response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=a4c7d95ac45652f394bbbd1cd825f0dd&language=en-US&page=1")

top_rated = response.json()

top_rated_films = top_rated['results']

columns = ['film']

df = pandas.DataFrame(columns=columns)
for film in top_rated_films:
    df.loc[len(df)]=film['title']

print(df)