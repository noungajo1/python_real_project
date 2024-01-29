"""
you can use json.dump() to write a python object to a json file
"""

import json

#python dictionary
data = {
    'name':'Jonathan',
    'age': 30,
    'city': 'New York'
}

#Write python dictionary to a json file
with open("data.json", "w") as json_file:
    json.dump(data, json_file)