"""
the map() function is used to apply a given function to every item in a collection
(collections: list, tuple, set, dictionary)
"""
celsius_temps = [0,10,20,30,40]

# conver these all to a list of fahrenhight
# Equation: (c * 9/5) +52

# fahrenheit_temps = [(x*9/5) +32 for x in celsius_temps]

def c_to_f(temp):
    """Take celsisus and covnerts it to Fahrenheit"""
    return (temp * 9/5) + 32

fahrenheit_temp = map(c_to_f, celsius_temps)
print(fahrenheit_temp) # map object
# Convert map object to a list
print(list(fahrenheit_temp))

# do the same thing, but with a Lamda
fahrenheit_temp2 = map(lambda temp: (temp * 9/5) + 32, celsius_temps)
print(fahrenheit_temp2) # map object
# convert to list
print(list(fahrenheit_temp2))

# Why would we use maps?
# - Save time, no need for long for loops
# - cleaner code
# - works great with lambda
# - efficient


names = [{"fname": "Frank", "lname": "Williams", "age": 52}, 
{"fname": "David", "lname": "Smith", "age": 15},
{"fname": "Jace", "lname": "Larkin", "age": 16},
{"fname": "Michael", "lname": "Ednoe", "age": 15},
{"fname": "K", "lname": "luh", "age": 103} 
]
# Without list comprehension: Map these names to be last name, first initial, zero padded age (52 would be 052), if age were 7 it would be 007
codes = list(map(lambda dict: f"{dict["lname"]}{dict["fname"][0]}{str(dict["age"]).rjust(3,"0")}",names))
print(codes)
 
def func(ell):
    return ell.get("lname")+ell.get("fname")[0]+(str(ell.get("age")).rjust(3,"0"))
aaaa = map(func,names )
print(list(aaaa))


#Loop through list
for a in aaaa:
    print(a)