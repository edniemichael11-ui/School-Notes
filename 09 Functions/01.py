# A function is a block of reusable code that performs a specific task
# ANY TIME YOU HAVE REPEATING CODE - rewrite it into a functions
# Why? Easier to read and maintain - less error prone




print("Mr. Klins is happy")
print("Mr. Klins is happy because ... well there's got to be a reason")
print("Mr. Klins is happy")

#If we wanted to print this t time look like this
#print("Mr. Klins is happy")
#print("Mr. Klins is happy because ... well there's got to be a reason")
#print("Mr>Klins is happy")
#print("Mr. Klins is happy")
#print("Mr. Klins is happy because ... well there's got to be a reason")
#print("Mr>Klins is happy")
#print("Mr. Klins is happy")
#print("Mr. Klins is happy because ... well there's got to be a reason")
#print("Mr>Klins is happy")
#print("Mr. Klins is happy")
#print("Mr. Klins is happy because ... well there's got to be a reason")
#print("Mr>Klins is happy")
#print("Mr. Klins is happy")
#print("Mr. Klins is happy because ... well there's got to be a reason")
#print("Mr>Klins is happy")


def mr_klins_is_happy():
    print("Mr. Klins is happy")
    print("Mr. Klins is happy because ... well there's got to be a reason")
    print("Mr. Klins is happy")

#says the block of code avoe 4 times
mr_klins_is_happy()
mr_klins_is_happy()
mr_klins_is_happy()
mr_klins_is_happy()

def someone_is_happy(person):
    print(f"{person} is happy")
    print(f"{person} is happy because ... well there's got to be a reason")
    print(f"{person} is happy")

someone_is_happy("Isaac")
someone_is_happy("Evan")
someone_is_happy("Allayn")

def someone_is(person, mood): #Person and mood are PARAMETERS
    print(f"{person} is {mood}")
    print(f"{person} is {mood} because ... well there's got to be a reason")
    print(f"{person} is {mood}")

someone_is("Sawyer", "sad") #Sawyer and Sad are ARGUMENTS that map to parameters
someone_is("Kluh", "Evil")
    
