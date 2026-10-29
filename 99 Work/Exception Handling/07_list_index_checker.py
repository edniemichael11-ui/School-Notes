animals = [
    "Dogs", "Cat", "Rabbit", "Duck", "Horse"
]

passed = False
while passed == False:
    try:
        index = int(input("Enter an index: "))
        print(animals[index])
        passed = True
    except IndexError:
        print("Invalid Index Entered")
    except ValueError:
        print("Enter an Integer")