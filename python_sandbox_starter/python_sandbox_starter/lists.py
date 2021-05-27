# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]

print(type(numbers))

print(numbers)

# Using a constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get 2nd value in the list
print(fruits[1])

# Length of the list
print(len(fruits))

# Append to the list
fruits.append('Mangos')

print(fruits)

# remove to the list
fruits.remove('Grapes')

print(fruits)

# insert into a certain position
fruits.insert(2, 'Strawberries')

print(fruits)

# remove from a certain position
fruits.pop(3)

print(fruits)

# Reverse List
fruits.reverse()

print(fruits)

# Sort List
fruits.sort()

print(fruits)

# Reverse Sort List
fruits.sort(reverse=True)

print(fruits)
