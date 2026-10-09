#The movie theater says senior discounts start at age 65, 
#but a 65-year-old is being charged $12. Let's use the debugger to figure out why.
print("Movie Ticket Calculator")

age = int(input("Enter your age: "))
tickets = int(input("How many tickets? "))

price = 12

if age < 18:
    price = 8
elif age > 65:
    price = 6

total = price * tickets

print(f"Price per ticket: ${price}")
print(f"Total: ${total}")

#to set a BREAKPOINT click in the gutter to the (left)
#in va code to next to the line you want to pause program execution

# Run the prgoram with run -> start deebugging or pressing f5 
# use step over f10 to toep over one line at a time
# Use continue f5 to just resume execution untila break point is hit again
# Use step into (f11) to go inside a function being called
 #use step out (shift + f11) to finish teh current function and return 