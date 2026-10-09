
productlist = []
quanityloop = []
priceloop = []

while True: 
 product_name =input("Product your buying: ").strip()
 
 price = input("How much does it cost: ")

 while True:
      quanity = input(f"How many {product_name} are you buying: ")
      if quanity.isdigit():
          quanity = int(quanity)
          break
      else:
          print("Invalid Quanity")

 productlist.append(product_name)
 quanityloop.append(quanity)
 priceloop.append(float(price))
 print("Enter Q to finish or C to continue")
 action = input("Action: ").upper()
 if action == "Q":
     break
 elif action == "C":
     continue
 else:
     print("Invalid Action")

subtotal = 0
subtotal_last = 0
print("Reciets")
for i in range(len(productlist)):
    print(f" Product:{productlist[i]}")
    print(f" Price: ${priceloop[i]:.2f}")
    print(f" Quanity:{quanityloop[i]}")
    subtotal = priceloop[i] * quanityloop[i]
    subtotal_last += subtotal
    print(f"Subtotal: ${subtotal:.2f}")



print(f"Subtotal: ${subtotal_last:.2f}")
tax = subtotal_last * 0.06
print(f"Tax (6%): ${tax:.2f}")
Total = subtotal_last + tax
print(f"Total: ${Total:.2f}")
