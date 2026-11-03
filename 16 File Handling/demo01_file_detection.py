"""
File detection means checking if a file or folder exist in the current workspace/given locations 
before your program tries to do anything with it

In Python, to work with files, you need the os module. The os module is for interacting with the Operating System
"""
import os

file_path = "demo_01_test.txt" #note this is a RELATIVE path
# Relative means, based on from the present working directory (where the program is running)


# See if our path exists:
if os.path.exists(file_path):
    print(f"The file path {file_path} exist")
else:
    print(f"The file path {file_path} DOES NOT exist")

file_path2 = "text_files/demo_01_test2.text"

if os.path.exists(file_path2):
    print(f"The file path {file_path2} exist")
else:
    print(f"The file path {file_path2} DOES NOT exist")

# bad
# file_path3 = "C:\Users\CMP_MIEdnie\Desktop\Coding\School Notes\Level 1 26-27\16 File Handling\text_files\demo_01_test2.txt"
# Works:
file_path3 = "C:/User/CMP_MIEdnie/Desktop/Coding/School Notes/Level 1 26-27/16 File Handling/text_files/demo_01_test2.txt" #forward slalshes
file_path3 = "C:\\Users\\CMP_MIEdnie\\Desktop\\Coding\\School Notes\\Level 1 26-27\\16 File Handling\\text_files\\demo_01_test2.txt" # double backslash
file_path3 = r"C:\Users\CMP_MIEdnie\Desktop\Coding\School Notes\Level 1 26-27\16 File Handling\text_files\demo_01_test2.txt"  #raw text file

if os.path.exists(file_path3):
    print(f"The file path {file_path3} exist")
else:
    print(f"The file path {file_path3} DOES NOT exist")

#detecting if it's a file or a folder:
file_path4 = r"C:\Users\CMP_MIEdnie\Desktop\Coding\School Notes\Level 1 26-27\16 File Handling\text_files\demo_01_test2.txt"
if os.path.exists(file_path3):
    if os.path.isfile(file_path3):
        print(f"The location {file_path3} is a file")
    elif os.path.isdir(file_path3):
        print(f"The location {file_path3} is a folder")

else:
    print(f"The file path {file_path3} DOES NOT exist")


#Detecting if a path is valid
# Determinig if it is a file or a directory
# relative vs absoulte paths.