from cerberus import Validator, errors

schema = {
    'name' : { 'type': 'string', 'required': True },
    'age': {'type': 'integer', 'min': 18, 'max': 99},
    'email': {'type': 'string', 'regex': r'\S+@\S+\.\S+', 'required': True}
}

validator = Validator(schema)

user_data = {
    'name' : 'John Doe',
    'age' : 23,
    'email': 'johndoe@gmail.com'
}

is_valid = validator.validate(user_data)

if is_valid:
    print("Data is valid")
else:
    print("Data is not valid")
