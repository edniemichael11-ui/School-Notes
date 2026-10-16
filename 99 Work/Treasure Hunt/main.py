import os
import Utilities
import random

def main():
    Utilities.getNonEmptyString()
    Utilities.pause()
    difficulty = ["Easy", "Medium", "Hard:"]
    Utilities.printNumberedList(difficulty)
    while True:
        Action = input("Action (1-3): ")
        if Action == 1:
            Treasure = 10
            trap = -5
            break
        elif Action == 2:
            Treasure = 20
            trap = -10
            break
        elif Action == 3:
            Treasure = 30
            trap = -20
            break
        else:
            print("Enter A valid Input (1-3)")
    print("Where would you like to dig")
    Locations = ["Dark Cave", "Sandy Beach", "Ancient Ruins"]
    Utilities.printNumberedList(Locations)
    Action = Utilities.getValidInt("Action: ", 1, 3)
    if Action == "1":
        loaction = "Dark Cave"
    elif Action == "2":
        location = "Sandy Beach"
    elif Action == "3":
        location = "Ancient Ruins"
    print(f" You dig at the {loaction} ")



if __name__ == "__main__":
    main()