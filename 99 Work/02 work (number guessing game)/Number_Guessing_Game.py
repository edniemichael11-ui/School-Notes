import random
MIN_VALUE = 1
MAX_VALUE = 100


def get_valid_int(prompt, min_value, max_value):
    while True:
        user_input = input(f"{prompt} ({min_value}-{max_value}): ").strip()
        """Make sure the users input is an int"""
        if user_input.isdigit() and min_value <= int(user_input) <= max_value:
            return int(user_input)
        print("Invalid guess. Please enter a whole number in the allowed range.")
def player_round(target):
    """This is the players round it will check the players guess and tell you if its to high or to low compared to the target number repeating until you get it. It also adds every number to a list"""
    guesses = []
    while True:
        guess = get_valid_int("What is your guess", MIN_VALUE, MAX_VALUE)
        guesses.append(guess)

        if guess > target:
            print("Too high!")
        elif guess < target:
            print("Too low!")
        else:
            print(f"Congrats, you got the number in {len(guesses)} guesses!")
            return guesses
def computer_round(target):
    """The computer round uses binary search to find the number, stores its gueses in a list and repeats until number is found"""
    low = MIN_VALUE
    high = MAX_VALUE
    guesses = []
    while True:
        guess = (low + high) // 2
        guesses.append(guess)
        print(f"Computer guesses: {guess}")

        if guess > target:
            print("Computer: too high")
            high = guess - 1
        elif guess < target:
            print("Computer: too low")
            low = guess + 1
        else:
            print(f"Computer got it in {len(guesses)} guesses!")
            return guesses
def print_outcome(player_guesses, computer_guesses, target):
    """Prints the outcome, the number, the players guesses, and the computer guess and determins a winner"""
    print("===== Final Results =====")
    print(f"Target Number: {target}")
    print()
    print("Player Guesses:")
    print(player_guesses)
    print(f"Player Guess count: {len(player_guesses)}")
    print()
    print("Computer Guesses:")
    print(computer_guesses)
    print(f"Computer Guess amount: {len(computer_guesses)}")
    print()

    if len(player_guesses) < len(computer_guesses):
        print("Winner: Player!")
    elif len(player_guesses) > len(computer_guesses):
        print("Winner: Computer!")
    else:
        print("It's a tie!")
def play_again():
    while True:
        choice = input("Would you like to play again? (Y/N): ").strip().upper()
        if choice in ("Y", "N"):
            return choice == "Y"
        print("Please enter Y or N.")


while True:
    target = random.randint(MIN_VALUE, MAX_VALUE)
    player_guesses = player_round(target)
    computer_guesses = computer_round(target)
    print_outcome(player_guesses, computer_guesses, target)

    if not play_again():
        print("Thanks for playing!")
        break
