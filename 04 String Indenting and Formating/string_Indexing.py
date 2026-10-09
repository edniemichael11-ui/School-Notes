print("""This is 
a long
long
long long long
long string
""")

#You can also just use the """ for a block comment (Multi-line)

"""
In python a string is just a sequence of characters.
Each Character has a position number, called an index
"""

"""
A byte is 8 bits. A bit is a 1 or a 0.
Eg. A byte might be 00110010
In memory everything must be stored in binary (1s or 0s)
"""

"""
Why string indexing is useful:
-Get individual charachters
-Get parts of a string (eg. First 5 charachters)
-Count from beggining or end
-Skip characters
-Reverse the string
"""
str1 = "abcdefghijklmnopqrstuvwxyz"
# index 0123456789
#What's the 5th chracter - note: Indexing starts at 0
print(str1[4]) #Use square brackets to acces by index. This will print 3, the 5th characters
print(str1[2])
#SLICING - used to get multiple characters
#format string[start:end]
print(str1[0:4]) #NOTE: the end value is exclusive
# this is the same:
print(str1[:4])

#lets get e through j
print(str1[4:10])

#Let's get j through the end
print(str1[9:]) #just add a colon and no number

#Negative indexing!
#Let's get just the last charachter
print(str1[-1])

#lets get the second to last
print(str1[-2])

# Let's get the last for charachters
print(str1[-4:])

# Skipping Characters
#Lets get just a,c,e
#(Start:End:Step)
print(str1[0::2])
#same as
print(str1[::2])

#Every 5th charachter starting with c
print(str1[2::5])

#Every 3rd charachter starting with b but not past v
print(str1[1:-4:3])

#Revere the entire strand
print(str1[::-1])