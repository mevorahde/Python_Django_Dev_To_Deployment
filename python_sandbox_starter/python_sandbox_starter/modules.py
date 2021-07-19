from typing import Text
import time
from datetime import date
import datetime
import camelcase
from validator import validate_email


# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager(including Django) as well as custom modules
# Core modules
# from time import time


today = datetime.date.today()

print(today)

today = date.today()

print(today)

timestamp = time.time()
print(timestamp)

# timestamp = time()
# print(timestamp)

# Pip modules

camel = camelcase.CamelCase()
text = 'hell there world'
print(camel.hump(text))

# Custom moduels
email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Not an email')
