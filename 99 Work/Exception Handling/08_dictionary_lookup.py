prices = {
    "Pizza": 12, 
    "Burger": 8,
    "Fries": 4, 
    "Soda": 2
}

print("1. Pizza")
print("2. Burger")
print("3. Fries")
print("4. Soda")
passed = False
while passed == False:
    try:
        Choice = input("Which food item: ").title()
        print(f"${prices[Choice]}")
        passed = True
    except KeyError:
        print("Invalid Item entered")