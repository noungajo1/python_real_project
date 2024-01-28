"""
a lambda function is a small, anonymous function defined usins the lambda keyword.
"""

#The syntax for a lambda function is as follow
x = 5
lambda arguments: x + 12

#Here is a simple example of a lambda function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print(result)  #Output: 8

#Here is an example using map() with a lambda function to square each element in a list
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) #Output: [1,4,9,16,25]