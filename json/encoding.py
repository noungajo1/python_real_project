"""
The json.dumps() function is used to encode a python object into a json
"""
import json

#python dictionary

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

#Convert python dictionary to json string

json_data = json.dumps(data)
print(json_data)