from match_operations import *

movie_csv = "movies.csv"


def play_random_matches():
    num_matches = input("How many matches to run?   ")
    fill_dict_from_csv(movie_csv)
    clear_csv(movie_csv)
    for i in range(int(num_matches)):
        print(f"({i+1})")
        run_match(make_random_match())
    fill_csv_from_dict(movie_csv)


def add_new_movie():
    new_title = input("What is the title of the movie?   ")
    fill_dict_from_csv(movie_csv)
    clear_csv(movie_csv)
    add_movie(new_title)
    print("10 matches to place new movie...")
    for i in range(10):
        print(f"({i+1})")
        run_match(give_movie_match(new_title))
    fill_csv_from_dict(movie_csv)


def print_top_movies(num_movies):
    for i in range(num_movies):
        print(sort_by_rating()[i])


def main():
    print("[1] Play random matches")
    print("[2] Add new movie")
    pick = input(">> ")
    if int(pick) == 1:
        play_random_matches()
    elif int(pick) == 2:
        add_new_movie()


if __name__ == "__main__":
    fill_dict_from_csv(movie_csv)
    print_top_movies(20)
    # main()
