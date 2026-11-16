import csv
filepath = "employees.csv"

with open(filepath, "r", newline = "") as file:
    content = csv.DictReader(file)
    #Skip header row
    next(content)
    for line in content:
        print(line)
        print(line["Name"])
    for line_num, line in enumerate(content):
        print(f"{line_num}: {line}")