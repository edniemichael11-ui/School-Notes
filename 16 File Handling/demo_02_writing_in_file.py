"""
Why write to files?
- hold information such as game scores, user settings, notes or logs, large data sets

3 common types of data files 
- plain text (.txt)
- comma sparated values (.csv)
- Javascript object notation (.json)
"""

#writing to a plain text file:
text_data = "um.... gibberish"
file_path = "text_files/demo_02_file01.text" #this is where we will save our data
"""
the preferred and safest wat to handle files is with the WITH statement
WITH will open the file and automatically close it (free the resources) even if a error occurs.
open is the function to open a file. "w" opens it in write mode.
note: with "w" if the file already exist, it will be overwritten
"""

with open(file_path, "w") as file: # must be exactly "w"
    file.write(text_data)


file_path2 = "../annoyinf file.text"
with open(file_path2, "w") as file:
    file.write("I am a super annoying file. Can you find me?")

#use with caution:
# delete a file:
import os
if os.path.exists(file_path2):
    os.remove(file_path2)


#but if we don't want to overwrite the file everytime?!
# Instead of using "w", we will use: "a", which stands for append
with open(file_path, "a") as file:
    file.write(
        "\nThe result of inflation on duck tokens has led to more trade and interest in baby ducks.")

# their is an "x" (exclusive creation) flag you can use, which will throw an error if the file already exist
# so if you want to create a file, but not overwrite one

try:
    with open(file_path, "x") as file:
        file.write("I am only here because a file didn't exist")
    print("File created succesfully")
except FileExistsError:
    print("That file already exists. No data Written")

colors = ["Blue", "Maroon", "Purple", "Red", "Green", "Yellow"]
#write thos each on there own line to a color.txt
file_path3 = "text_files/color.txt"
with open(file_path3, "w") as file:
    for color in colors:
        file.write(f"\n{color}")