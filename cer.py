from cerberus import Validator

schema = {
    'name' : { 'type': 'string', 'required': True , 'minlength':4},
    'age': {'type': 'integer', 'min': 18, 'max': 99},
    'email': {'type': 'string', 'regex': r'\S+@\S+\.\S+', 'required': True},
    'phone': { 'type': 'string', 'min': 10, 'max':10 },
    'gender': { 'type': 'string', 'allowed': ['male', 'female', 'other'], }
}

validator = Validator(schema)

user_data = {
    'name' : 'Joh',
    'age' : 22,
    'email': 'johndoe@gmail.com',
    'phone': '9861601060',
    'gender': 'male'
}

is_valid = validator.validate(user_data)

if is_valid:
    print("Data is valid")
else:
    for field, error in validator.errors.items():
        print(field, error)
