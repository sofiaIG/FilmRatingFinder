import imdb
import rotten_tomatoes_client
import argparse
import sys


moviesDB_IMDb = imdb.IMDb()
moviesDB_rotten = rotten_tomatoes_client.RottenTomatoesClient


def args_parser(args):
    my_parser = argparse.ArgumentParser(description="Name of the film and date of release")
    my_parser.add_argument("Film",
                       metavar="film",
                       type=str,
                       help="the film title")
    try:
        my_parser.add_argument("Date",
                       metavar="date",
                       type=int,
                       help="release date of the film")
    except:
        my_parser.error("The date needs to be an integer")
    return my_parser.parse_args(args)
    # if args.Date <0:
    #     my_parser.error("The date needs to be an integer")




def testing_something(args):
    input_title = args.Film
    input_date = args.Date
    return [input_title,input_date]


def search_score_rotten(user, year_release):
    movie_search = moviesDB_rotten.search(user)
    accessing_movies = movie_search["movies"]
    for movie in accessing_movies:
        name = movie["name"]
        year = movie["year"]
        if name.lower() == user.lower() and year == year_release:
            return movie["meterScore"]


def find_movie_imdb(year_of_release, user):
    movie_search = moviesDB_IMDb.search_movie(user)
    for movie in movie_search:
        year = movie['year']
        if int(year) == year_of_release:
            return movie


def search_ratings_imdb(year_release, user):
    movie_found = find_movie_imdb(year_release, user)
    id = movie_found.getID()
    movie = moviesDB_IMDb.get_movie(id)
    rating = movie['rating']
    return rating

args = args_parser(sys.argv[1:])
print(args)
list_input =testing_something(args)
title = list_input[0]
year = list_input[-1]
score_rotten = search_score_rotten(title, year)
score_imdb = search_ratings_imdb(year, title)

if score_rotten is None and score_imdb is None:
    print("Film not found")
    sys.exit()
print(f"The film {title} is rated {score_imdb} on IMDB and {score_rotten} on rotten tomatoes.")

