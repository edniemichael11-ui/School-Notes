import json

try:
    with open("many_people.json", "r") as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("JSON file not found")

#print out Nami abd Pirate from data
print(data[0]["name"])
print(data[0]["job"])
print("\n")
for record in data:
    print(record["name"])
    print(record["age"])
    print(record["job"])







# MEGA CHALLENGE
