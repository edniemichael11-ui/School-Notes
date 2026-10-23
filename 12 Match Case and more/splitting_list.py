import random
import time
mystr = "This is a sentence about the hobgoblin Jace"
list_of_words = mystr.split() # if we specify nothing, it will split on " "
print(list_of_words)
list_of_words[-1] = "Mykyta"
print(list_of_words)
mystr = " ".join(list_of_words)
print(mystr)
# Simulated csv
str2 = "name, type, strength, health"
p1 = "michael, elf, 3, 200"
p2 = "isaac, loot goblin, 2, 100"

headers = str2.split(",")
p1_list = p1.split(",")
p2_list = p2.split(",")

# Iterate through p1 list index and value
for idx, val in enumerate(p1_list):
    print(f"{headers[idx]}: {val}")
print()
for idx, val in enumerate(p2_list):
    print(f"{headers[idx]}: {val}")

playerlist = [p1_list, p2_list]
p1_list.append(0)
p2_list.append(0)
print(f"Its the big battle of {p1_list[0]} Vs {p2_list[0]}")
input("Press enter to continue!")
for i in range(5):
    print(f"Round {i+1}")
    choice = random.randint(0,2)
    outcomes = []
    if choice < 2:
        attacker = playerlist[choice]
        defender = playerlist[1-choice]
        outcomes.append(attacker[0])
        playerlist[choice][-1] += 1
        print(f"{attacker[0]} delievered {attacker[2]} damage to {defender[0]} and defeated him/her")
    else:
        outcomes.append("tie")
        print("It was a tie")
    time.sleep(3)



print(f"{p1_list[0]} won {p1_list[-1]} rounds")
print(f"{p2_list[0]} won {p2_list[-1]} rounds")
if p1_list[-1] > p2_list[-1]:
    print(p1_list[0], "Won!")
elif p1_list[-1] < p2_list[-1]:
    print(p2_list[0], "Won!")
else:
    print("Its a tie")
