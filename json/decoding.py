import json

#json formatted string
json_data = '{"name":"John","age":30,"city":"New York"}'

#Convert json string to python dictionary
data = json.loads(json_data)
print(data)