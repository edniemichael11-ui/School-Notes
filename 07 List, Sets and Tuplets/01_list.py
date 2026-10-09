#Sometime we want to store miltiple peices of related data
#Python has special data structures called collections
#A collection is a single variable that stores multiple values
#Four types of collections:
#1. Lists
#2. Sets
#3. Tuples
#4. Dictionaries


#Lists:
#Imagine we want to store multiple types of fruits
#We could have variables, fruit1, fruit2, fruit3......
#That canm be tough to deal with and messy.
#Instead we use lists []

fruits = ["apple", "orange", "banana", "starrwberry"]
print(fruits)
#How do we access a specific element - eg. "Orange"?
print(fruits[1]) #notice list are 0 index
#We can change a value
fruits[1] = "Kiwi" 
print(fruits[1])

#Slicing a list
#Extract a range of items from a list:
sublist = fruits[1:3] #Takes item 1 and 2
print(sublist)
# You can even use step values
print(fruits[::2])
# Reverse the list
print(fruits[::-1])

# Looping through a list:
for var in fruits:
    print(var)

# A few useful methods:
#Add elemt to a list at the end:
fruits.append("dragon fruit")
print(fruits)

#rempove an element from a list
fruits.remove(fruits[1]) #pass ina  value
#same as fruits.remove("kiwi")
print(fruits)

# Inset an element:
# put the element wherever we want it (in range)
fruits.insert(2, "mango")
print(fruits)

# Sort the list:
fruits.sort()
print(fruits)
# count instances of a value:
print(fruits.count("banana"))

#find the index of a value
print(fruits.index("mango"))

#find the length of a list:
print(len(fruits))

# clear the list:
fruits.clear()
print(fruits)
