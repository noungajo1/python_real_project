"""
a dictionary is a mutable, unordered collection of key-value pairs.
dictionaries are useful for storing and retrieving data in a structured way
"""

# Creating an empty dictionary

empty_dict = {}

# Creating a dictionary with key-values pairs

my_dict = {'name':'Jonathan','age':25,'City':'Yaounde'}

#Accessing values
print(my_dict['name'])   #Output: 'Jonathan'
print(my_dict['City'])  #Output: 'Yaounde'

#Modifying values

my_dict['age'] = 31

#Adding a new key-values pair
my_dict['occupation'] = 'Engineer'

#Removing a key-value pair using del
del my_dict['City']

#Removing and retrieving a value using pop
removed_value = my_dict.pop('occupation')

#Dictionary methods
keys = my_dict.keys()      #Returns a list of keys
values = my_dict.values()  #Returns a list of values
items = my_dict.items()    #Returns a list of key-value pairs as tuples

print(keys)
print(values)
print(items)

#Iterating over keys
for key in my_dict:
    print(key)

#Iterating over values
for value in my_dict.values():
    print(value)

#Iterating over items (key-value pairs)
for key, value in my_dict.items():
    print(f"{key}: {value}")
