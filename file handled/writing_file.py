file_path = 'example.txt' #the file is suppose to exist
with open(file_path, "w") as file:
    file.write('Hello, this is a test.\n')
    file.write('Writing to a file in python.\n')