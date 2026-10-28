products = [
    {"name": "Keyboard", "price": 45},
    {"name": "Monitor", "price": 180},
    {"name": "Mouse", "price": 25},
    {"name": "Headphones", "price": 75},
    {"name": "USB Drive", "price": 15},
    {"name": "Webcam", "price": 60}
]

cheap = list(filter(lambda price: price["price"] <= 50, products))
print("Products under $50: ")
for products in cheap:
    print(f"{products["name"]} - ${products["price"]}")