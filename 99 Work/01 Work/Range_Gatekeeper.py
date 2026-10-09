invalid_attempts = 0

while True:
    lvl_num = input("What level are you: ").strip()
    
    if not lvl_num.isdigit():
        invalid_attempts += 1
        print(f"Invalid, attempt {invalid_attempts}")
        continue
        
    lvl_num = int(lvl_num)
    
    if 10 <= lvl_num <= 50:
        print("You have passed the gate")
        break
    else:
        invalid_attempts += 1
        print(f"Invalid, attempt {invalid_attempts}")

