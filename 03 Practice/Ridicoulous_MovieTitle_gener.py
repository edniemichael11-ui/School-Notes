movie = input("Enter a movie title: ").strip() 
boring_word = input("Enter a boring word: ").strip() 
funny_word = input("Enter a funny replacement: ").strip()


print(f"Original: {movie.title()}")
print(f"The word appeared {movie.count(boring_word)} time (s)")
print(f"New Movie: {movie.replace(boring_word, funny_word)}")
