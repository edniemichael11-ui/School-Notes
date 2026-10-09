#Let's get some input!
name= input("Enter your name:")

print(f"hello, {name}")

#Dealing with number input

age=input("Enter your age: ")
#We need to cover age to a number
#Casting!!!!
age=int(age)  #this convers the string to an int
print(f"This year you are {age}, next year you will be {age+1}")

shoes=input("Enter the cost of your shoes: ")
#We want shoes to be a float
shoes=float(shoes)

print(f"The cost of your shoes with 6% tax is {shoes*1.06:.2f}")