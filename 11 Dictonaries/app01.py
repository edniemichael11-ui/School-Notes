"""
A Dictionary is one of four main collection types
Main collection types
-List: A Container that can hold several items, editable, and ordered [item1, item2, item 3]
-Dictionary: A vontainer that cold hold several key/value pairs. Each key connects to a value {"klins": 899. "Winchell": 85}
-Tuple: A container that can hold several items, NOT editable and ordered (item1, item2, item3)
-Set: A container that holds several UNIQUE items. Editable in the form of add/remove but not ordered {item1, item2, item3}
"""

Zach_capitals = {
    "Pennsylvania": "Allentown",
    "Texas": "Dallas",
    "Florida": "Miami",
    "New York": "Jamestown",
    "Wisconsin": "Madison"
}

# print(dir(Zach_capitals)) #List all avauble dictionary methods
# help(Zach_capitals)

#Accessing values:
print(Zach_capitals["Florida"])
# print(Zach_capitals["Ohio"])
# We can safely try to acces a value by an unconfirmed key with .get
print(Zach_capitals.get("Ohio"))
print(Zach_capitals["Florida"]
      if "Florida" in Zach_capitals else "Not Found")

# Let's fix zach_capitals:
Zach_capitals["Wisconsin"] = "Green Bay"
print(Zach_capitals)
# Either updates and existing record, or creating a new one
Zach_capitals.update({"Wisconsin": "Madison"})

#if statements to handle if key exist
if Zach_capitals.get("Ohio"):   #Dictionarys are case sensitive
    print(Zach_capitals["Ohio"])
else:
    print("Not found in the dictionary")


#Remove Items
Zach_capitals.__delitem__("Florida")
print(Zach_capitals)
#more common approach:
Zach_capitals.pop("Texas")
print(Zach_capitals)

#Empty the dictionary:
# Zach_capitals.clear()
# print(Zach_capitals)

# Getting all keys values from a disctionary
print(Zach_capitals.keys()) # Looks like a list, but its a "Dictionary view object", but you can iterate over it
for key in Zach_capitals.keys(): # Iterate over the keys
    print(key)


print(Zach_capitals.values()) # Gives backa dictionary values object, also iterable
for value in Zach_capitals.values():
    print(value)


print("\nWhat's this?")
for item in Zach_capitals:
    print (Zach_capitals[item], item)


# We want to iterate over all keys and values
for states, capital in Zach_capitals.items():
    print(f"{capital}, {states}")