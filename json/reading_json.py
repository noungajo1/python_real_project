"""
you can use json.load() to read a json file into a python object
"""

import json

#Read python object from a json file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)