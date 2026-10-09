#isDigit 
str1 = "123"
print(str1.isdigit()) #print true if they are numbers
print("123.5".isdigit()) # False

print("123".isalpha()) #false
print ("dog".isalpha()) #true
print ("dog1".isalpha()) #False

#count: Counts the number of character occurence
str2 = "Mr Klins just keeps typing and typing and typing!"
#how many "t"s?
print(str2.count("t"))
print(str2.count("typing"))

str3 = "Mr Klins is making us work"
print(str3.replace("work", "take a break"))