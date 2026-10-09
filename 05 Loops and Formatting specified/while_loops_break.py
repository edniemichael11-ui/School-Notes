import random
#
while True:
    print("Infinite")
    choice = input ("Enter I for and insult, or Q to quit: ").capitalize()
    if choice == "I":
        #come back and write insult code
        print(f"You are a {random.choice(["Stink", "Dumb Dumb", "Terrible human beaing", "waste of flesh"])}")
    elif choice == "Q":
        break #This will exit the loop
    else:
        print("That was not a valid option")
print("Thanks for being a good sport")