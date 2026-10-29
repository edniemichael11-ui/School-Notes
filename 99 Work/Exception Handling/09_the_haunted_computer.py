import random
import time
creepy_messages = [
    "Look Behind you",
    "Do you hear it scratching inside",
    "I Know what you did",
    "Its in the walls",
    "It's behind you"
]
displayed = 0
while displayed <5:
    try:
        time.sleep(1)
        print(creepy_messages[random.randint(0,5)])
    except IndexError:
        print("ERROR: Something is trying to communicate...")
    finally:
        print("The computer is watching you")
        print("")
        displayed += 1
