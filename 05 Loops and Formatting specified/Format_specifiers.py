# Format specifiers are special codes that tell Python how to format 
# (or style) numbers when printing them — especially when using f-strings
price = 3.14159

#To Two decimal places 
print(f"{price} to 2 decimals places (.2f) {price:.2f}")
print(f"{price} to 4 decimals places (.2f) {price:.4f}")
print(f"{price} cosuming 10 number of spaces (right aligned) (:10) {price:10}")
print(f"{price} cosuming 10 number of spaces (right aligned) (:010.2f) ZERO PADDED and two decimal point {price:010.2f}")
#Alignments:
print(f"Left: ####{price:<10.2f}####")
print(f"Right: ####{price:>10.2f}####")
print(f"Centered: ####{price:^10.2f}####")

newnum = 100987
#showing positive and negative signs
print(f"{newnum:+}")
newnum *= -1 #Makes the num negative
print(f"{newnum:+}")

#comma as thousand sparator
print(f"{newnum:,}")

# putting many togethor:
print(f"{price:>+10,.2f}")