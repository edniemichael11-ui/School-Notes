import json
with open("rick_and_morty.json", "r") as file:
    data = json.load(file)
 
alive = list(filter(lambda x :  x["status"] == "Alive", data["results"]))
 
with open("alive_characters.json","w") as file:
    json.dump(alive, file, indent = 4)