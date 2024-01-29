file_path = 'example.tx'
try:
    with open(file_path,'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found')
except IOError:
    print('Error reading the file.')