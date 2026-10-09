code = input("Enter a code: ").strip()

if code[0].upper() == "A" and len(code)==5:
   
    print("Valid")
   
else:
    print("Invalid")