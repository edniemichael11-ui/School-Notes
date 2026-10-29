shopping_list = []
total = 0
while True:
    try:
        item = input("Enter item price (Q to quit): ")
        if item.upper() == "Q":
            break
        price = float(item)
        if price < 0:
            raise ValueError("Price cannot be negative")
        total += price
        shopping_list.append(price)
        print("Item added!")
    except (ValueError, TypeError):
        print("Invalid Price")
    finally:
        print("Item Processed")
print(f"Items Purchased: {len(shopping_list)}")
print(f"Total: ${total:.2f}")

