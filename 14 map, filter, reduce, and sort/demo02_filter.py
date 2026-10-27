"""
Filter: Similiar to map, only the function returns True or False
"""

names = ["isaac", "david", "jace", "zach", "evan"]
print(names)

def is_not_zach(name):
    return name.lower().strip() != "zach"

cleaned_list = list(filter(is_not_zach, names)) # returns filtered object
print(cleaned_list)

even_better = list(filter(lambda name: name.lower().strip() != "jace", cleaned_list))
print(even_better)



grades = [
    {"Students": "Evan", "Score": 12},
    {"Students": "Isaac", "Score": 83},
    {"Students": "Kaine", "Score": 90},
    {"Students": "Blake", "Score": 79},
    {"Students": "Michael", "Score": 89},
    {"Students": "Zach", "Score": 4}
]


# filter this lsit down to only passing students:
passing_students = list(filter(lambda grade: grade["Score"] >= 60, grades))
print(passing_students)