"""
In Python, keyword arguments are arguments that are preceded by an identifier (the parameter’s name) when you call a function.
They make your code easier to read and allow you to change the order of arguments when calling a function.
"""
def hello(greeting, title, first, last):
    print(greeting, title, first, last)

#Call the function with positional argument, the order matters
hello("Hello","Mr.", "Evan", "Burlingame")
#What happens if we change
hello("Evan", "hello", "Burlingame", "Mr.")
# Try again with keyword arguments
hello(first = "Evan", greeting = "Hello", last = "Burlingame", title = "Mr.")

# Note: you can mix, but positional args must be first:
hello("Hello", "Mr.", last = "Birlingame", first = "Evan")