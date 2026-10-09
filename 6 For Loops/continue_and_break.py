#print the numbers 1 through 20, but skip 13
for x in range (1,21):
    if x == 13:
        continue
    else:
        print(x, end = " ")


print()
#stop the loop if we hit 13
for x in range (1,21):
    if x == 13:
        break
    else:
        print(x, end = " ")