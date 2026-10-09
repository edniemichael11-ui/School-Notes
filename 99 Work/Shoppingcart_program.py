Item=input("What item are you buying: ")
Price=input("What is the price: ")
Amount=input("How many are you buying: ")
Price=float(Price)
Amount=int(Amount)

total=(Price*Amount)

print(f"You bought {Amount} {Item}")
print(f"Your total is {total}")