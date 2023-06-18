from pydantic import BaseModel, ValidationError, validator

user = {
        'name': 'Sandeep',
        'age': 25,
        'email': 'sandeep@gmail.com'
    }

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

    @validator('age')
    def validate_age(cls, age):
        if age < 18 or age > 100 :
            raise ValueError('age should be between 18 and 100')
        return age
    
    @validator('name')
    def validate_name(cls, name):
        if len(name) < 4 or len(name) > 50:
            return ValueError('Name length should be more than 4 and less than 50')
        return name
        
    @validator('email')
    def validate_email(cls, email):
        if '@' not in email or not email.endswith('.com'):
            raise ValueError('Email doesnt follow proper email format')
        return email
        
    
    
    

try:
    valid = UserProfile(**user)
    print(valid)

except ValidationError as e:
    print(e)