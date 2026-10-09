# List comprehensions provide a concise, readable and efficient way to create new lists

# General Format:
# [expression for item in iterable if condition] 
# #iterable is something like a list, tuple, or dictionary
# expression: what you want to do with each item (eg. x * 2)
# for item in iterable: the loop that goes through each value (eg. for x in range(1,11))
# if condition: (optional): A filter that decides which items to include

#example (traditional method - without list comprehension):
doubles = []

for x in range(1, 11):  # range(1, 11) gives numbers 1–10
    doubles.append(x * 2)

print(doubles) 

# simplify the aboe, and do it in one line!
doubles_lp = [x*2 for x in range(1,11)]
print(doubles_lp)

#note , we can unpack list by prepending a * to them.
mykytas_query =  [*[x*2 for x in range(1,11)], 99]
print(mykytas_query)
mykytas_query += [x*2 for x in range(1,11)]
print(mykytas_query)

#Let's say we only want multiples of 5
#lets do it without a step function on range
multiples_of_5 = [x for x in range(0,51) if x % 5 == 0]
print(multiples_of_5)

games = ["call of duty", "fortnite", "mindsutry", "no man's sky"]
#use list comprehension to creat a list of these titles in title case.
game_title = [games.title() for games in games]
print(game_title)

#update the above to only give back tittles with more then one word
game_title = [games.title() for games in games if " " in games.strip()]
print(game_title)

students = [("Zach", 54 ), ("Christian", 0), ("Evan", 1), ("K-luh", 106), ("Blake", 80), ("Allyn", 90)]
#use list comphrension toc reate a list of students who have a score of over 70
good_grades = [x for x in students if x[1] >= 70]
print(good_grades)
bad_grades = [x for x in students if x[1] <= 70]
print (bad_grades)