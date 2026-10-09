# A set is a collection that is unordered, immatable, AND:
# DOES NOT ALOOW DUPLICATES
fruits = {"apple", "orange", "banana"}
#Outputs may not always be the same because they are unordered
print(fruits)

# key methods:
fruits.add("coconut")
print(fruits)

fruits.remove("apple")
print(fruits)

#fruits.remove("apple") #error thrown because apple is no longer there

#Remove a random element:
elem = fruits.pop()
print(fruits)
print(f"element removed: {elem}")

# clear the set:
fruits.clear()
print(fruits)
