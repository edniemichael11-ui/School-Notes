total = 0
valid_changes = 0
while True:
    change = input("How much change: ").strip()
    if change.isdigit():
        change = int(change)
        total += change
        valid_changes +=1
    else:
        print("Invalid Change")

    

    if total >= 100:
        print(f"Total: {total}")
        print(f"Valid Entries: {valid_changes}")
        if total == 100:
            print("You landed exactly on 100")
        else:
            print("you went over 100")
        break
    else:
        continue




