Name = input("What is your first name: ").strip()
Name = Name.capitalize()
Snack = input("What Snack do you want: ").strip().title()
snack_price = input("Price of snack: ").strip()
snack_quanity = input(f"How many {Snack} do you want: ")
snack_price = float(snack_price)
snack_quanity = int(snack_quanity)
subtotal = snack_quanity*snack_price
discount = 0

if subtotal > 10:
    discount = subtotal*0.10
else:
    discount = 0

Final_Total = subtotal-discount

print("Receipt")
print(f"Customer: {Name}")
print(f"Snack: {Snack}")
print(f"Quantity: {snack_quanity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Total : ${Final_Total:.2f}")