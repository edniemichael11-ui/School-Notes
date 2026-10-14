# Imports
import random
import msvcrt
import time
import os

#Variables
game_running = True
Num_of_Ran_letters = 4
Random_string = []
Level = 1
Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


#Functions
def clear_screen():
    """Clears the Screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_keyboard_buffer(): 
    """Prevents keyboard buffers"""
    """Remove any pending keystrokes from the keyboard buffer.""" 

    while msvcrt.kbhit(): 

        msvcrt.getwch()

def generate_random_guess():
    """Generates Random Guess"""
    Random_string = []
    letters_generated = 0
    while letters_generated < Num_of_Ran_letters:
        Random_string.append(random.choice(Letters))
        letters_generated += 1
    return Random_string

def quit_or_continue():
    """Ask you whether you want to quit or start the game"""
    Action = input("Press Q to quit or anything else to start the game: ").strip().capitalize()
    if Action == "Q":
        print("have a good day")
        return False
    else:
        return True

def get_user_guess():
    """Gets the User Guess and prints the random number"""
    print(f"Level: {Level}")
    print("-".join(Random_string))
    dots = 0
    while dots < 5:
        print(".", end = "", flush = True)
        time.sleep(1)
        dots += 1
    clear_screen()
    clear_keyboard_buffer()
    user_guess = input("Enter what you just saw (Does not need to be capitilized): ").strip().upper()
    return user_guess

def check_if_guess_is_correct():
    """Checks if Player Guess is correct"""
    if user_guess.upper() == "".join(Random_string):
        print("Correct")
        return True
    else:
        return False

def Game_over():
    """Prints the Game Over Messages"""
    Completed_Level = Level - 1
    print("Incorrect!")
    print(" ")
    correct_string = "".join(Random_string)
    print(f"Correct String: {correct_string}")
    print(f"Your Awnswer: {user_guess}")
    print(" ")
    print(f"You successfully made it through level: {Completed_Level}")
    if Completed_Level <= 2:
        print("Wow, did you understand the Game?")
    elif Completed_Level >= 3 and Completed_Level <=6:
        print("Not Bad, keep working on it")
    else:
        print("Nice Job! You're a memory master!")

def play_again():
    """Ask the user to play again"""
    Action= ""
    while True:
        Actions = input("Would you Like to play again (Y/N): ").strip().upper()
        if Actions == "N":
            print("Have a good day")
            return False
        if Actions == "Y":
            return True
        else:
            print("Invalid Entry try again")


# Game Loop
game_running = quit_or_continue()
while game_running == True:
    Random_string = generate_random_guess()
    user_guess = get_user_guess()
    if check_if_guess_is_correct() == False:
        Game_over()
        play_again_choice = play_again()
        if play_again_choice == True:
            Level = 1
            Num_of_Ran_letters = 4
            continue
        else:
            game_running = False
    else:
        Level += 1
        Num_of_Ran_letters += 1
        continue
