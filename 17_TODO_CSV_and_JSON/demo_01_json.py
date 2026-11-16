"""
JSON (JavaScript Object Notation) is a popular format for storing structured data
It uses key-value pairs, similiar to: Dictionaries in python
example:
{
"name": "Nami",
"age": 35,
"job": "Pirate"
}

In python to work with json, you may need to import json
"""
import json
#writing json file:
person = {
"name": "Nami",
"age": 35,
"job": "Pirate"
}

file_path = "people.json"
with open(file_path, "w") as file:
    json.dump(person, file, indent = 4)

print(f"JSON file ({file_path}) created siccessfully")

many_people = [
    {
    "name": "Nami",
    "age": 35,
    "job": "Pirate"
    },
    {
    "name": "Jace",
    "age": 53,
    "job": "Banker"
    },
    {
    "name": "K-Luh",
    "age": 35,
    "job": "SuperVillian"
    }
]
with open("many_people.json", "w") as file:
    json.dump(many_people, file, indent = 4)


