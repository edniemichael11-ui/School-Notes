print("Hello, World!")

#Hashtags in Python can be used for line comments
#This will not be run or interpreted by Python.

#Our First variable
first_name = "Bill" # This is a string. It is surrounded with quotes ""
print(first_name)
sport= "Cross Country"

#fstrings - allow you to embed variables into strings
print(f"{first_name} likes {sport}")

#int (or integer) demo:
age= 100
# " Bill likes cross country and he is 100 years old"
print(f"{first_name} likes {sport} and he is {age} years old")

#floats (decimal numbers)
gpa = 1.89
print(f"unfortunatly, {first_name}'s gpa is {gpa}")

# booleans (true/false)
# more often used for conditional logic
allowed_to_play = True
print(f"{first_name} is alloweed to play: {allowed_to_play}")

#demo of an if statement!
if allowed_to_play:
    print(f"{first_name} is allowed to play! Huzzah!")
else:
    print (f"{first_name} cannot play. What a bum.")

  