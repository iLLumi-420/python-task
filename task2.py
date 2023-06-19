user_profile_dict = {
    'age': 25,
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'gender': 'male',
    'address': '123 Main St',
    'phone': '9861601060'
}

validation_rules_array = [
    {
        'field': 'name',
        'type': str,
        'rules': [
            {'name': 'min_length', 'value': 3},
            {'name': 'required', 'value': True},
        ]
    },
    {
        'field': 'age',
        'type': int,
        'rules': [
            {'name': 'min_value', 'value': 18},
            {'name': 'max_value', 'value': 99}
        ]
    },
    {
        'field': 'email',
        'type': str,
        'rules': [
            {'name': 'min_length', 'value': 5},
            {'name': 'max_length', 'value': 50}
        ]
    },
    {
        'field': 'gender',
        'type' : str,
        'rules': [
            {'name': 'valid_values', 'value': ['male', 'female']}
        ]
    },
    {
        'field': 'phone',
        'type': str,
        'rules': [
            {'name': 'length', 'value': 10},
        ]
    },
    {
        'field': 'address',
        'type': str,
        'rules': [
            {'name': 'required', 'value': False},
            {'name': 'max_length', 'value': 50}
        ]
    },
]


def validate(dict, validation_rules_array):
    for field_rules in validation_rules_array:
        field = field_rules['field']
        field_type = field_rules['type']
        value = dict.get(field)

        if(type(value) != field_type):
            print('Type error')
            return False
        
        for rules  in field_rules['rules']:
            rule_name = rules['name']
            rule_value = rules['value']      
            
            if rule_name == 'min_length':
                if len(value) < rule_value:
                    print(f'length should be minimun {rule_value}')
                    return False
            elif rule_name == 'max_length':
                if len(value) > rule_value:
                    print(f'length should be maximum {rule_value}')
                    return False
            elif rule_name == 'min_value':
                if value < rule_value:
                    print(f'value should be minimun {rule_value}')
                    return False
            elif rule_name == 'max_value':
                if value > rule_value:
                    print(f'value should be maximum {rule_value}')
                    return False
            elif rule_name == 'valid_values':
                if value not in rule_value:
                    print(f'{value} is not valid')
                    return False
            elif rule_name == 'required':
                if rule_value:
                    if value is None:
                        print(f'Required field is empty')
                        return False
            elif rule_name == 'length':
                if len(value) != rule_value:
                    print(f'Phone number length should be {rule_value}')
                    return False
    
    return True

                

print(validate(user_profile_dict, validation_rules_array))

