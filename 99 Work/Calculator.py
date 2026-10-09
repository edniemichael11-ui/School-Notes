num1 = int(input("First number: "))
operator = input("Operation(+,-,/,*,%): ")
num2 = int(input("Second number: "))

if operator == "+":
    endnum = num1 + num2
    print(endnum)
elif operator == "-":
    endnum = num1 - num2
    print(endnum)
elif operator == "/":
    endnum = num1 / num2
    print(endnum)
elif operator == "*":
    endnum = num1 * num2
    print(endnum)
elif operator == "%":
    endnum = num1 % num2
    print(endnum)
else:
    print("invalid operation")