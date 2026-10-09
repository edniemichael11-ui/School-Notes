AtC_P = int(input("Attack Power? "))
Mon_def = int(input("Monster Defense? "))
damage = AtC_P - Mon_def

if damage >= 50:
    print("CRITICAL HIT!")
elif damage >= 20:
    print("Solid Hit")
elif damage > 0:
    print("Weak Hit")
else:
    print("The Monster laughs at your attack")

print(f" You dealt {damage} damage.")
