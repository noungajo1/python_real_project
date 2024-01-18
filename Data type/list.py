"""
a list is a mutable, orderes collection of element, it can contain
items of different data types
"""

# Creating an empty list

emty_list = []

# Creating a list with elements

my_list = [1,2,3,'apple','banana',True]

#accessing elements

print(my_list[0])  #Output:1
print(my_list[3])  #Output: 'apple'

# Negative indexing

print(my_list[-1])   #Output: True

# Modifying elements

my_list[1] = 'orange'
print(my_list) #Output: [1, 'orange', 3, 'apple','banana', True]

# adding elements

my_list.append('grape')  # appends 'grape' to the end
print(my_list)

my_list.insert(2, 'kiwi')   #insert 'kiwi' at index 2
print(my_list)

another_list = ['pear', 'peach']
combined_list = my_list + another_list   # concatenating two lists
print(combined_list)

#  Romoving elements

my_list.remove('orange')  # removes the first occurrence of 'orange'
print(my_list)

popped_element = my_list.pop(2)  #removes and returns the element at index 2
print("popped element {}".format(popped_element))
print(f"my list {my_list}")

# list functions

length = len(my_list)
maximum = max([1,2,3,5,4,6,8])
minimum = min([2,1,4,5,9,0,5])
total = sum([4,2,9,5])
print(f"length {length} maximum {maximum} minimum {minimum} Total {total}")

# all list function
print(dir(my_list))