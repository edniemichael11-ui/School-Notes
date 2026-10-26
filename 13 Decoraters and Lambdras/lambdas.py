"""
A lambda function in Python is a small, anonymous function
- anonymouse mean it has no name
- Usually run once and discared (on the fly)
Key Facts about Mandas
The can take any numbe of arguments 
They can contain only on expression (single line of code)
They are commonly used with *higer- order functions* like map(), filter() and reduce(), which are functions that take other functions as arguments
Basic Syntax: 
lambda parameters: expression
eg. lambda x: x* 2
"""
# Example 1:
double = lambda x: x*2

print(double(2)) #4
print(double(3)) #6


add = lambda x, y: x + y

print(add(3,4)) #7
print(add(4,5)) #9
