"""
To open a file, we use open() function. it takes two arguments
the file name and the mode. modes include r for reading, w for writing and a for appending
b for binary files for +
"""

#Open a file for reading : the file should exist
file_path = "example.txt"
#Read the entire content of the file
with open(file_path,"r") as file:
    content = file.read()
    print(content)
#File is automatically closed whrn exiting the with block

#Read a single line from the file:the first line is read
with open(file_path, "r") as file:
    line = file.readline()
    print(line)

#Read all lines into a list
with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)