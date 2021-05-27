# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple Dictionary
person = {
    'first_name': 'David',
    'last_name': 'Mevorah',
    'age': 32
}

print(person)

# Using a constructor

person2 = dict(
    first_name='Steph',
    last_name='Curry',
    age=33
)

print(person2)

# Access single value
print(person['first_name'])
print(person.get('last_name'))

# Add Key/Value
person['phone'] = '555-555-5555'

print(person)

# Get just the keys

print(person.keys())

# Get just the values

print(person.values())

# Get the pair values
print(person.items())

# Make a dict copy
person3 = person.copy()
person3['city'] = 'Fremont'

print(person3)

# Removing an item

del(person['age'])
person.pop('phone')

print(person)

# Get the length of the dictionary
print(len(person))

# Clear the dictionary
person.clear()

print(person)

# List of dictionaries

people = [

    {'first_name': 'Barry', 'last_name': 'Bonds', 'age': 50},
    {'first_name': 'Jerry', 'last_name': 'Rice', 'age': 55}
]

print(people)

print(people[1]['first_name'])
