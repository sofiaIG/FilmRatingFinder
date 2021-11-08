import imdb
import argparse
import rotten_tomatoes_client
import argparse
import sys


moviesDB_IMDb = imdb.IMDb()
moviesDB_rotten = rotten_tomatoes_client.RottenTomatoesClient

my_parser = argparse.ArgumentParser(description="Name of the film and date of release")

my_parser.add_argument("Film",
                       metavar="film",
                       type=str,
                       help="the film title")

my_parser.add_argument("Date",
                       metavar="date",
                       type=int,
                       help="release date of the film")

args = my_parser.parse_args()
input_title = args.Film
input_date = args.Date


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


def search_filmratings_imdb(year_release, user):
    movie_found = find_movie_imdb(year_release, user)
    id = movie_found.getID()
    movie = moviesDB_IMDb.get_movie(id)
    rating = movie['rating']
    return rating


score_rotten = search_score_rotten(input_title, input_date)
score_imdb = search_filmratings_imdb(input_date, input_title)
if score_rotten == None and score_imdb == None:
    print("Film not found")
    sys.exit()
print(f"The film {input_title} is rated {score_imdb} on IMDB and {score_rotten} on rotten tomatoes.")

