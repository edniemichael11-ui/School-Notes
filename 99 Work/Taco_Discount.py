num_taco = int(input("How many tacos would you like? "))
taco_price = float(input("Price of Taco? "))
age = int(input("Age? "))


if num_taco >= 10 and age < 18:
    discount = taco_price * 0.25
elif num_taco >= 10 or age < 18:
    discount = taco_price * 0.10
else:
    discount = 1

Origonal_tot = num_taco * taco_price
final_tot = Origonal_tot * discount + Origonal_tot

print(f"Original total: ${Origonal_tot}")
print(f"Final total: ${final_tot}")