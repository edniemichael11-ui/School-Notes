"""
A decorator in Python is a function that extends the behavior of another function without modifying it

-Takes a base function as input
-Adds extra code or functionality before or after that base function runs
-Returns a new function that combines both behaviors
"""
# Base Function:
def get_ice_cream():
    """Gives you Ice Cream"""
    print("Here is your Ice Cream")


# create a simple decorator
# A decorator is just a function that takes another function as an arugment
def add_sprinkles(func):
    #define a function that we will return (commonly called wrapper):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        #call the function that was passed in:
        func(*args, **kwargs)
    return wrapper #note we are not returning a result of wrapper, we are returning the function itself

#update this code to have an add_fudge decorator
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add Fudge")
        func(*args, **kwargs)
    return wrapper 


# it is common to build your decorators to accept 
# *args and **kwargs to work with functions that may take params
@add_sprinkles
@add_fudge
def get_ice_cream_decorated(flavor):
    """Gives you Ice Cream"""
    print(f"Here is your {flavor} Ice Cream")




if __name__ == "__main__":
    get_ice_cream_decorated("Chocolate")