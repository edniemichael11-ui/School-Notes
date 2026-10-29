"""
Exception: What is thrown when an error in you r applications occurs>
Crashes your programs 


str = "Cheese"
if str > 1:
    print(5)
TypeError: '>' not supported between instances of 'str' and 'int'

print(4/0)
ZeroDivisionError: division by zero

print(int("A"))
ValueError: invalid literal for int() with base 10: 'A'

coolFunction
NameError: name 'coolFunction' is not defined

Try: the code block that is potentially dangerous
Except: The code to runif an exception occurs
Finally: the block of code that runs after a try/except either way
"""
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please enter a valued Integer")

# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     print(num1/num2) 
# except (ZeroDivisionError, ValueError) as e:
#     print(f"an error occurred: {e}")


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valued Integer")
finally:
    print("Operation complete")