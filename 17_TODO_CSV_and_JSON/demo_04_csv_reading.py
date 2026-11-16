import csv

filepath = "employees.csv"

with open(filepath, "r", newline = "") as file:
    content = csv.reader(file) # louds everything as a csv reader object
    #print(content)
    for line in content:
        print(line)
        print(line[0]) #acces a specific field of the csv