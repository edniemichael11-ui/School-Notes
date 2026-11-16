#CSV: Comma separated Values
import csv


employees = [
    ["Name", "Age", "Job"],
    ["SpongeBob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

#Write the 2d list to files:
with open("employees.csv", "w") as file:
    writer = csv.writer(file)
    # loop through our 2d list and record to file
    for row in employees:
        writer.writerow(row)
    writer.writerow(["Mr. Klins", 99, "Corpse, Plant Food" ])

print(f"CSV file Writeen")



#write it all at once
with open("employees_2.csv", "w") as file:
    writer = csv.writer(employees)
    writer.writerow(employees)
    print(f"CSV file Writeen")