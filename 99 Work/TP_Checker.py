age = int(input("How old are you: "))
height = int(input("How tall are you(inches): "))

if age >= 12 and height >= 54:
    print("You may ride The Pythonator!")
    print(f"Age:{age}  Height:{height}")
elif age>= 12 and height < 54:
    print("You are old enough but to short.")
    print(f"Age:{age}  Height:{height}")
elif age< 12 and height >= 54:
    print("You are tall enough but to young")
    print(f"Age:{age}  Height:{height}")
else:
    print("sorry your not ready for The Pythonator")
    print(f"Age:{age}  Height:{height}")