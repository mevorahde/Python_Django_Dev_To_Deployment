# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def say_hello(name='Sam'):
    """
    Print Hello and then name.
    """
    print('Hello ' + name)


say_hello('David')
say_hello()

# Return value


def get_sum(num1, num2):
    total = num1 + num2
    return total


num_sum = get_sum(2, 3)
print(num_sum)


def add_one_to_num(num):
    num += 1
    return num


num = 5
new_num = add_one_to_num(num)
print(new_num)

# A lambda function is a small anonymous function.


def get_sum_lambda(num1, num2): return num1 + num2


print(get_sum_lambda(9, 2))
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
def add_one_to_num_lambda(num): return num + 1


print(add_one_to_num_lambda(5))
