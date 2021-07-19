# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


class Customer (User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of a {self.balance}'


# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 27)

print(brad.name)
print(brad.age)

# Edit property
brad.age = 38
print(brad.age)

print(janet.email)

janet.has_birthday()

# Call method
print(janet.greeting())

# Init customer
john = Customer('John Doe', 'john@gmail.com', 40)
john.set_balance(500)

print(john.name)
print(john.balance)
print(john.greeting())
