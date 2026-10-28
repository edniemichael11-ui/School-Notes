movies = [
    ("The Matrix", 1999),
    ("Avatar", 2009),
    ("Jurassic Park", 1993),
    ("Avengers: Endgame", 2019),
    ("Inception", 2010),
    ("Titanic", 1997)
]

movies.sort(key = lambda movie: movie[1])
print("Movies (Newest to Oldest)")
for pos, movie in enumerate(movies):
    print(f"{movies[pos][0]} - {movies[pos][1]}")