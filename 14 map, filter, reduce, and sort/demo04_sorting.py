names = ["Evan", "Jace", "Zach", "Mykyta", "Isaac", "Allyn"]
# We can sort the list with the .sort method
# note: this changes the actual order of your list
print(names)
names.sort() #default to alphabetifcal (all capitals first)
print(names)

#sort in reverse order
names.sort(reverse=True)
print(names)

other_names = ("blake", "michael", "abigale", "josie", "ryan", "josh", "duane", "john")

# other_names.sort() # can't change a tuple!
# print(other_names)
# but we can sort a tuple if we use sorted
sorted_other_names = sorted(other_names)
# Sorted returns a new list, instead of sorting in place
print(sorted_other_names)

#sort by length of string:
len_of_name_sorted = sorted(other_names, key=len)
print(len_of_name_sorted)

most_vowels = sorted(other_names, key = lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s))), reverse=True)
 
print(most_vowels)


def get_last_letter(word):
    return word[-1]

sorted_by_last_letter = sorted(other_names, key = get_last_letter)
print(sorted_by_last_letter)
