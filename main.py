import imdb
import rotten_tomatoes_client
moviesDB_IMDb = imdb.IMDb()
moviesDB_rotten = rotten_tomatoes_client.RottenTomatoesClient

def user_input():
    user = input("Enter tha name of the film: ")
    year_release = int(input("Enter the year of release: "))
    values = [user, year_release]
    return values

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


values = user_input()
user = values[0]
year_release = values[1]
score_rotten = search_score_rotten(user, year_release)
score_imdb = search_filmratings_imdb(year_release, user)
print(f"The film {user} is rated {score_imdb} on IMDB and {score_rotten} on rotten tomatoes.")


