#Append to a file
file_path = 'example.txt'
with open(file_path,'a') as file:
    file.write("Appending additional content.\n")