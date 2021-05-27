# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = "David"
age = 32


# Concatenate
print("Hello, I am " + name + " and I am " + str(age) + " years old.")

# String Formatting

# Arguements by position
print("Hello, I am {} and I am {} years old.".format(name, age))

# Arguements by name
print("Hello, I am {name} and I am {age} years old.".format(
    name="Tom", age=41))

# F-Strings (only in 3.6+)
print(f"My name is {name} and I am {age}")

# String Methods
s = "hello there world."

# Capitalize first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get variable length
print(len(s))

# Replace method
print(s.replace('world', 'everyone'))

# Count
sub = "h"

print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
