"""
a tuple is an ordered, immutable collection of element. Once
you create a tuple, you cannot modify its content. Tuples are often
used for grouping related data together
"""

# Creating an empty tuple

empty_tuple = ()

#creating a tuple with elements
my_tuple = (1,2,'apple','banana',True)

# Accessing elements
print(my_tuple[0])   #Output: 1
print(my_tuple[2])   #Output: 'apple'

# Negative indexing

print(my_tuple[-1])  #Output; True

#Tuple unpacking
a,b,c,d,e = my_tuple
print(a,b,c,d,e)

# Trying to modify a tuple (this will raise an error)
# my_tuple[0] = 5
# TypeError: 'tuple' object does not support item assignment

#tuple functions
lenght = len(my_tuple)
maximum = max((1,5,2,8))
minimum = min((3,6,1,7))
total = sum((4,2,9,5))
print(lenght,maximum, minimum,total)

# Returning multiple values from a function using a tuple
def get_coordinates():
    return(3.14,2.71)

x, y = get_coordinates()
print(x,y)