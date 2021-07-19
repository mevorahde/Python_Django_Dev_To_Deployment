# Python has functions for creating, reading, updating, and deleting files.


# Open a file
my_file = open('myfile.txt', 'w')

# Get some info
print('Name: ', my_file.name)
print('Is Closed: ', my_file.closed)
print('Opening Mode: ', my_file.mode)

# Write to file
my_file.write('I love Python')
my_file.write(' and Javascript')
my_file.close()

# Append to file
my_file = open('myfile.txt', 'a')
my_file.write(', I also like CSS')
my_file.close()

# Read form file
my_file = open('myfile.txt', 'r+')
text = my_file.read(10)
print(text)
