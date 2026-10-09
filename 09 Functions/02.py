#Functions that RETURN things
purchases = [2.99, 5.99, 7.99]
def calculate_total(prices, tax):  #Prices will be a list of float, tax will a float
    """ This is a *super awesome* function returns your total"""
    total = sum(prices)
    total = total + (total * tax)
    return total #Notice the RETURN statement, passes the value back

my_total = calculate_total(purchases, .06)
print(f"{my_total:.2f}")

def get_user_in_within_range(min,max):
    """Prompts the user to enter a value between *min* and *max* (exclusive)"""
    while True:
        t = input(f"Enter a number between {min:int} and {max:int}: ")
        if t.isdigit():
            if int(t) >= min and int(t) < max:
                print("Good job.")
                break
        print("Invalid, Try again.")
    return int(t)

mynum = get_user_in_within_range(1, 100)


while True:
    num = get_user_in_within_range(1, 100)
    if num == 5:
        break



