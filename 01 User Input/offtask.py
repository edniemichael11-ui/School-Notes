import random
Names=["Evan", "Mykyt", "jace", "Duane", "Allyn"]
adjectives= ["smart", "a horrible person", "carnivorous", "cheesy", "boring", "dumb" ]

for element in Names:
    print(f"{element} is {random.choice(adjectives)}")