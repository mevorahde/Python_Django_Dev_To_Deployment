import json

# Sample JSON
user_JSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(user_JSON)

print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

car_JSON = json.dumps(car)

print(car_JSON)
