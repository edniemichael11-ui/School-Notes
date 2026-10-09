phrase = input("Enter a phrase: ").strip()
phrase_first = phrase[0:4]
phrase_last = phrase[-3:]
print(phrase[::2])
print(f"First 3 Characters: {phrase_first}")
print(f"Last 3 Characters: {phrase_last}")