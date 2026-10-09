str1 = "Until we meet again"
#find() : finds the First occurrence of a character
print(str1.find(" ")) #returns of INDEX of the first occurence
print(str1.find("U"))
print(str1.find("M")) #-1 means it was not found!
#but what if we dont care about casing?!
#let's CHAIN some methods
print(str1.upper().find("M"))

#find the last occurrence of a character in a string:
#rfind
print(str1.rfind("i"))

#example of y/n input where we wanted Y or N
y_n = "  y     "
y_n = y_n.strip().upper()
print("It's valid!" if y_n == "Y" or y_n == "N" else "Invalid")

name = "jason"
print(name.capitalize()) #capitalizes first letter

title = "the hunger games"
print(title.title()) #capitilizes the first letter of each word
