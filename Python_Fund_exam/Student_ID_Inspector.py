ID = input("What is your student ID: ").strip().upper()
IDlen = len(ID)
Schoolcode = ID[0:2]
StudentNumber = ID[3:]
Lasttwo = ID[6:]

if not IDlen == 8:
    print("Invalid - ID must be exactly 8 characters")
elif not Schoolcode.isalpha() == True:
    print("Invalid ID - First 2 characters must be letters")
elif not StudentNumber.isdigit() == True:
    print("Invalid ID = Last 6 characters must be numbers")
else:
    print(f"Valid ID - Masked ID:{Schoolcode}****{Lasttwo}")