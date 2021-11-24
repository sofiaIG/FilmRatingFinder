# FilmRatingFinder
This CLI (command-line) program finds film ratings for you from IMDb
and Rotten Tomatoes and displays them. It is small and fast!


## How to use
```bash
python main.py "Name of the film" Year
```

e.g.:
```bash
python main.py "cape fear" 1991
```

## Installing dependencies
The tool has two basic dependencies - imdbpy and rotten_tomatoes_client.
Poetry configuration is in place, and a requirements.txt is also
available if you want to install globally or manage your virtual
environment differently.

### Installing dependencies using Poetry
Assuming Poetry is already install, you only need to change into the
code's directory and run:
```bash
poetry install
poetry shell
```

### Installing dependencies using pip
Unless you specifically want to install globally, you should probably
first create and activate a virtual environment. Then you can simply change
into the code's directory and run:
```bash
pip -r requirements.txt
```
