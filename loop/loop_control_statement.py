fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    if fruit == 'banana':
        break
    print(fruit)

#Example with continue
    
numbers = [1,2,3,4,5]

for num in numbers:
    if num %2 == 0:
        print('I continue')
        continue
    print(f'the number is {num}')