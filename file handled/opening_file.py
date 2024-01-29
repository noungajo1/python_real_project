"""
To open a file, we use open() function. it takes two arguments
the file name and the mode. modes include r for reading, w for writing and a for appending
b for binary files for +
"""

#Open a file for reading : the file should exist
file_path = "example.txt"
with open(file_path,"r") as file:
    content = file.read()
    print(content)
#File is automatically closed whrn exiting the with block
