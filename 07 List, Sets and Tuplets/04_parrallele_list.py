#parallel list:
#the value at an index is one list, align with the value in another

names = ["christian", "duane", "allyn", "zach"]
ages = [15, 19, 31, 52]

for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

while True:
    for i in range(len(names)):
        print(f"{i}: {names[i]}")
    idx = input(f"Enter an index of the person whose age'd like. Q to quit:  ").strip()
    indx = int(idx)
    if idx.lower == "q":
        break
    else:
        print(f"{names[idx]} is {ages[idx]} years old")


