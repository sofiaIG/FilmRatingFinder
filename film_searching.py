import imdb
import rotten_tomatoes_client
import argparse
import sys


def args_parser(args):
    my_parser = argparse.ArgumentParser(description="Name of the film and date of release")
    my_parser.add_argument("Film",
                       metavar="film",
                       type=str,
                       help="the film title")
    my_parser.add_argument("Date",
                       metavar="date",
                       type=int,
                       help="release date of the film")
    return my_parser.parse_args(args)


def title_date(args):
    input_title = args.Film
    input_date = args.Date
    return [input_title,input_date]


def search_score_rotten(user, year_release):
    movie_search= rotten_tomatoes_client.RottenTomatoesClient.search(user)#THIS
    accessing_movies = movie_search["movies"]
    for movie in accessing_movies:
        name = movie["name"]
        year = movie["year"]
        if name.lower() == user.lower() and year == year_release:
            return movie["meterScore"]


def find_movie_imdb(year_of_release, title):
    moviesDB_IMDb = imdb.IMDb()
    movie_search = moviesDB_IMDb.search_movie(title)#THIS needs to be done here
    for movie in movie_search:
        year = movie['year']
        if int(year) == year_of_release:
            return movie_search


def search_filmratings_imdb(year_release, title):
    moviesDB_IMDb = imdb.IMDb()
    movie_found = find_movie_imdb(year_release, title)
    rating = 0
    if movie_found != None:
        movie_found_elements = movie_found[0]
        id = movie_found_elements.getID()
        movie = moviesDB_IMDb.get_movie(id)
        rating = movie['rating']
    return rating

if __name__ == '__main__':
    args = args_parser(sys.argv[1:])
    list_input =title_date(args)
    title = list_input[0]
    year = list_input[-1]
    score_rotten = search_score_rotten(title, year)
    score_imdb = search_filmratings_imdb(year, title)



    if score_rotten is None and score_imdb is None:
        print("Film not found")
        sys.exit()
    print(f"The film {title} is rated {score_imdb} on IMDB and {score_rotten} on rotten tomatoes.")
