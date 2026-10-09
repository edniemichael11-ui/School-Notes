import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function whenever you need it
clear_screen()


import time
mystr = input("Enter a string to print out: ")
while(mystr == ""):
    mystr = input("Enter a string for me to type back out: ").strip()
#note:A loo will be better for this,but were looking at it with string indexing

#print("line 1\nline 2\nline 3\n newline - advance to the next line")
index = 0
clear_screen()
while index < len(mystr):
    print(mystr[index], end="", flush=True) #by default, end is a \N
    time.sleep(.2)
    index += 1
