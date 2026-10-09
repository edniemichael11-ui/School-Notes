password = input("Enter the robot password: ") 
print(f"Cleaned Password: {password.strip()}")
print(f"Lenght: {len(password)}") 
print(f"Only Digits {password.isdigit()}")
print(f"Only Letters {password.isalpha()}")
print(f"Number of 7's : {password.count("7")}")
print(f"Last 7's Location: {password.find("7")}")
 
if password == "ROBOT7": 
    print("ACCESS GRANTED") 
else: 
    print("ACCESS DENIED")