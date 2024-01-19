#Identity Operators

x = [1,2,3]
y = [1,2,3]

z = x
#is
print(x is y)  #False, because x and y are different objects
print(x is z)  #True, because x and z reference the same object

#is not
print(x is not y)  #True, because x and y are different objects
print(x is not z)  #False, because x and z reference the same object

#Membership operators

my_list = [1,2,3,4,5,6,7,8]

#in
print(3 in my_list)  #True, because 3 is present in the list
print(12 in my_list)  #False, because 12 is not present in the list

#not in
print(3 not in my_list)  #False, because 3 is present in the list
print(12 not in my_list)  #True, because 12 is not present in the list