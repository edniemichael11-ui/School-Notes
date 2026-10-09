# String - "a line of text", A series of characters
# methods - a function you can run (python has built in methods)
# example of a string
str1 ="I like apples and bananas"

#getting input retrieves a string
name = input("Enter your full name: ")

#the len() function:
#returns the length of the string
print(len("dog")) #3
print(len(name)) #the length of the input

#leading and trailing spaces can throw things off!
# Ex. If we are looking for a y or n and user inputs " Y" or "Y " ......
y_or_n = input ("Please enter a y or a n: ")

if y_or_n == "y":
    print("you entered y")
else:
    print("thats not a y!")

#let's get rid of leading and trailing spaces!

y_or_n = y_or_n.strip()

if y_or_n == "y":
    print("you entered y")
else:
    print("thats not a y!")
