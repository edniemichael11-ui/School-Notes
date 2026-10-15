"""
Modules are an extremely useful tool for ogranizing and reauisng code.
Simple put, a module is a python file that contains code, variables, functions, classes 
that you can include in another program
Just like functions Modules help make your code:
-reusable
-organized
-easier to maintain

DRY Principle - Don't Repeat Yourself

Examples of built in modules:
time, random, os, math......

eg.
import math #including the module
print(math.pi) #using code from the imported module
"""


##Lets see the built in modules:
#import math
#help(math)

#import a module with an alias
import math as m
print(m.pi)

# We could also import just specific functions from a moodule
from random import randint
print(randint(1,10))