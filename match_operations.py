from movie import *
from elo_system import *
import csv
import random
from operator import itemgetter

movies = []
movie_csv = "movies.csv"


def sort_by_rating(descending=True):
    if descending:
        return sorted(movies, key=lambda x: float(x["rating"].replace(",", "")), reverse=True)
    else:
        return sorted(movies, key=lambda x: float(x["rating"].replace(",", "")))


def add_movie(title):
    movies.append({"title": title, "rating": "1000"})


def give_movie_match(movie_to_match):
    while True:
        random_dict = movies[random.randint(0, len(movies)-1)]
        if random_dict['title'] != movie_to_match:
            return [Movie(movie_to_match, next(item for item in movies if item['title'] == movie_to_match)['rating']),
                    Movie(random_dict['title'], random_dict['rating'])]


# returns a list of 2 movie objects randomly chosen from the list of dictionaries (movies)
def make_random_match():
    sample = random.sample(range(0, len(movies)-1), 2)
    return [Movie(movies[sample[0]]['title'], movies[sample[0]]['rating']),
            Movie(movies[sample[1]]['title'], movies[sample[1]]['rating'])]


# given a movie, change it's corresponding rating
def modify_rating(movie_title, new_rating):
    next(item for item in movies if item['title'] == movie_title)['rating'] = new_rating


def run_match(matchup):
    m1 = matchup[0]
    m2 = matchup[1]
    while True:
        print(f"[1]   {m1.title}")
        print(f"[2]   {m2.title}")
        winner = input(">> ")
        if winner == "1":
            clear_csv(movie_csv)
            match(m1, m2, m1)
            modify_rating(m1.title, m1.elo)
            modify_rating(m2.title, m2.elo)
            fill_csv_from_dict(movie_csv)
            return m1
        elif winner == "2":
            clear_csv(movie_csv)
            match(m1, m2, m2)
            modify_rating(m1.title, m1.elo)
            modify_rating(m2.title, m2.elo)
            fill_csv_from_dict(movie_csv)
            return m2
        else:
            print(f"{winner} is not a valid response.")


# transfer movies and their corresponding ratings into the movies list from the csv file
def fill_dict_from_csv(filename):
    # open movies.csv as DictReader
    with open(filename, mode='r') as file:
        csv_file = csv.DictReader(file)
        # line by line, copy movies & ratings
        for lines in csv_file:
            movies.append(lines)


def clear_csv(filename):
    # clear movies.csv of all text
    with open(filename, mode='w') as file:
        file.truncate(0)


def fill_csv_from_dict(filename):
    # transfer list of dictionaries (movies) back into movies.csv
    with open(filename, mode='w') as file:
        csv_file = csv.DictWriter(file, ["title", "rating"], extrasaction='ignore')
        csv_file.writeheader()
        for movie in movies:
            csv_file.writerow(movie)
