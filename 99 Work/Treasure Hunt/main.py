
import os
import Utilities
import random
import time

def main():
    
    game_ended = False
    Explorer = Utilities.getNonEmptyString("Enter Username: ")
    Utilities.pause()
    while True:
        difficulty = ["Easy", "Medium", "Hard"]
        Utilities.printNumberedList(difficulty)

        while True:
            Action = input("Action (1-3): ")

            if Action == "1":
                Treasure = 10
                trap = -5
                break
            elif Action == "2":
                Treasure = 20
                trap = -10
                break
            elif Action == "3":
                Treasure = 30
                trap = -20
                break
            else:
                print("Enter A valid Input (1-3)")

        rounds = 1
        score = 0
        rounds_score = []

        while game_ended == False:
            print("====Treasure Hunt ====")
            print(f"Round {rounds} of 5")
            print("Where would you like to dig")

            Locations = ["Dark Cave", "Sandy Beach", "Ancient Ruins"]
            Utilities.printNumberedList(Locations)

            action = Utilities.getValidInt("Action: ", 1, 3)

            if action == 1:
                location = "Dark Cave"
            elif action == 2:
                location = "Sandy Beach"
            elif action == 3:
                location = "Ancient Ruins"

            print(f"You dig at the {location}")

            hidden = ["Trap", "Nothing", "Treasure"]
            hidden_item = random.choice(hidden)
            if hidden_item == "Trap":
                rounds_score.append(trap)
                print(f"It was a trap! (score {trap})")
                score += trap

            elif hidden_item == "Nothing":
                rounds_score.append(0)
                print("Nothing is here")


            elif hidden_item == "Treasure":
                print(f"You found Treasure! (score {Treasure})")
                rounds_score.append(Treasure)
                score += Treasure

            print(f"Current Score: {score}")
            time.sleep(2)
            Utilities.clearScreen()
            rounds += 1

            if rounds > 5:
                game_ended = True

        print("==== Treasure Report ====")
        print(f"Explorer: {Explorer}")
        print(f"Round 1: {rounds_score[0]}")
        print(f"Round 2: {rounds_score[1]}")
        print(f"Round 3: {rounds_score[2]} ")
        print(f"Round 4: {rounds_score[3]}")
        print(f"Round 5: {rounds_score[4]}")
        pos_nums,pos_ammount,neg_ammount, zero_ammount = Utilities.analyzeNumbers(rounds_score)
        print(f" Treasure Rounds: {pos_ammount} | Trap Rounds: {neg_ammount} | EMpty Rounds: {zero_ammount}")
        print(f"Total Score: {score}")
        if score < 0:
            print("Lost Explorer")
        elif score >= 0 and score <=19:
            print("Beginner Explorer")
        elif score >= 20 and score <= 49:
            print("Treasure Hunter")
        elif score >= 50:
            print("Master Treasure Hunter")
        play_again = input("Would you like to play again (Y/N): ").strip().capitalize()
        if play_again == "N":
            return False
        else:
            continue



if __name__ == "__main__":
    main()
