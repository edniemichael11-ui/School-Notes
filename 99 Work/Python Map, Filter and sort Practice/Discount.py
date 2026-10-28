prices = [25.00, 50.00, 75.00, 100.00, 150.00] 
print(f"{prices:.2f}") 
def discount_price(price): 
    discount = price * 0.20 
    return price - discount 
price_discount = list(map(discount_price, prices)) 
print(f"{price_discount:.2f}") 