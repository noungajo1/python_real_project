"""
a set is an unordered mutable collection of unique elements
"""

#Creating an empty set
empty_set = set()

#Creating a set with elements
my_set = {1, 2, 3, 4, 5}
print(my_set)

#Adding elements to a set
my_set.add(6)
print(my_set)

#Removing elements from a set
my_set.remove(3)  #Raises an error if the element is not present
my_set.discard(3)  #Removes the element if present, otherwise does nothing

#Set operations

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

union_set = set1.union(set2)  #{1,2,3,4,5,6,7}
intersection_set = set1.intersection(set2)  #{3,4,5}
difference_set1_set2 = set1.difference(set2)  #{1,2}
print(difference_set1_set2)
difference_set2_set1 = set2.difference(set1)  #{6,7}
print(difference_set2_set1)
symmetric_difference_set = set1.symmetric_difference(set2)  #{1,2,6,7}

