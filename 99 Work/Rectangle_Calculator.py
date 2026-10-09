while True: 
    choice=input("Are you calculating (Area or Volume): ").strip()

    if choice=="Area":
        R_length=input("Enter the length of the rectangle: ")
        R_width=input("Enter the width of the rectangle: ")
        Unit=input("What is the Unit measurment: ")
        R_length=float(R_length)
        R_width=float(R_width)
        R_Area=(R_length*R_width)
        print(f"The area is {R_Area} square {Unit} ") 
        break
    elif choice=="Volume":
        R_length=input("Enter the length of the rectangle: ")
        R_width=input("Enter the width of the rectangle: ")
        R_height=input("Enter the height of your rectangle: ")
        R_length=float(R_length)
        R_width=float(R_width)
        R_height=float(R_height)
        R_Volume=(R_length*R_width*R_height)
        print(f"The volume of the rectangle is {R_Volume}")
        break

    else:
        print("Error: You must type Volume or Area.")
