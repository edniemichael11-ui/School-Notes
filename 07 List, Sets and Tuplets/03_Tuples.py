# A tuple is a collection that is ordered and unchangeable
# Faster than lists
# Use parenthesis ()

fruits = ("apple", "orange", "banana", "apple")
print(fruits)
print(fruits[1])

#methods:
print(fruits.count("apple"))
print(fruits.index("orange"))

for fruit in fruits:
    print(fruit)


"""
Use a list when you need an ordered, editable group of items.
Use a set when you need unique items with no duplicates.
Use a tuple when you need an ordered group that never changes and you want it to be fast.
"""
