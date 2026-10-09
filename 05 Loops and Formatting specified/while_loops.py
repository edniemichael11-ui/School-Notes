# A while loop in Python is used to repeat a block of code as long as a certain condition is true.
#format:
#while boolean expression that evalutes to true:
# code to execute

# we want a number from a user:
num = input("Enter a whole number: ").strip()
print(num.isdigit())

while not num.isdigit():
    num = input("Enter a whole number: ").strip()
print("Good Job")

pw = ""
while pw != "Until we meet again":
    pw = input("Please enter the password: ")
print("Access granted!")

#make sure age is valid (not negative)
age = int(input("Enter your age: "))
while age < 0:
    print("Invalid Age")
    age = int(input("Enter your age:"))
print("Congratulations, your alive!")

# Infinite loops
grade = int(input("Enter your grade (less than 70 sends us to infinite loop): "))
while grade < 70:
    print("You're failing. Enter a new grade : ")
    #students often forget to assign a new value, so this could go forever!





