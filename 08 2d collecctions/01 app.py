# 2d stands for Two Dimensional
#eg. A 2d list is made of a list of Lists
# This type of structure is very handy when you want to orgranize data in a grid or matrix (rows and columns)

charachters = ["mario", "sonic", "woody"]
movies = ["Super Mario Movie", "Sonic the Hedgehog", "Toy Story"]
likeability = [8, 7, 10]

# lets makea a 2d list of that:
movie_data = [charachters, movies, likeability]

#Study It:
print(movie_data)
print(movie_data[1]) #access the movies list
print(movie_data[2][2]) #acces the 10 in the likeability list

#think of it like coordinates

#each list does not have to parallel or the same lenght

groceries =[
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]

#print me apple
print(groceries[0][0])

#print me fish
print(groceries[2][1])