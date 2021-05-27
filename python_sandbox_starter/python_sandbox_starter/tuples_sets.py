# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# A simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

print(fruit_tuple)

# Using the constructor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

print(fruit_tuple)

# Get single value
print(fruit_tuple[1])

# Can not change value
# fruit_tuple[1] = 'Grape'  # Will throw error

# Tuples with one value should have trailing coma
fruit_tuple2 = ('Apple', )

print(fruit_tuple2)

# Get length of tuple
print(len(fruit_tuple2))

# delete tuple
del fruit_tuple2

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}

print(fruit_set)

# Check if in the set
print('Apple' in fruit_set)
print('Apples' in fruit_set)

# Add to a set
fruit_set.add('Grape')

print(fruit_set)

# Remove to a set
fruit_set.remove('Grape')

print(fruit_set)

# Clear the set
fruit_set.clear()

print(fruit_set)

# Delete the set
del fruit_set
