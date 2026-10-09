Message = input("Input Message: ").strip()

print(f"Lenght: {len(Message)}")
print(f"First: {Message[0:1]}")
print(f"Last: {Message[-1:]}")
print(f"First 3: {Message[0:3]}")
print(f"Last 3: {Message[-3:]}")
print(f"Every 2nd character: {Message[0::2]}")
print(f"Reversed: {Message[::-1]}")