password = "Cheese"
attempts = 3
while True:
    password_attempt = input("What is your password: ")
    if password_attempt == "Cheese":
        print("Access Granted")
        break
    else:
        attempts -=1
        print(f"Incorrect, {attempts} attempts remaining")

    if attempts == 0:
        print("ran out of Attempts")
        break

    