x = True
y = False

#Logical AND
result = x and y  #False
print(result)

#Logical OR
result = x or y  #True
print(result)

#Logical NOT
result = not x  #False
print(result)

age = 25
is_student = False

#Logical AND
if age > 18 and not is_student:
    print("You are an adult who is not a student.")

#Logical OR
if age < 18 or is_student:
    print("you are either under 18 or a student.")