passed = False
while passed == False:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(num1/num2)
        passed = True
    except ValueError:
        print("Invalid Value")
    except ZeroDivisionError:
        print("You cant divide by zero")
