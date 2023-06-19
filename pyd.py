from pydantic import BaseModel, ValidationError, validator
import re

user = {
        'name': '25654',
        'age': 25 ,
        'email': 'san.deep123_@gmail.com',
        'gender': 'male',
        'phone' : '9861601060'
    }

class UserProfile(BaseModel):
    name: str 
    age: int
    email: str
    gender: str
    phone: str
    
    @validator('name', pre=True)
    def validate_name(cls, name):
        if not isinstance(name, str):
            raise ValueError('Name must be string')
        if len(name) < 4 or len(name) > 50:
            raise ValueError('Name length should be more than 4 and less than 50')
        return name

    @validator('age')
    def validate_age(cls, age):
        if age < 18 or age > 100 :
            raise ValueError('age should be between 18 and 100')
        return age
        
    @validator('email')
    def validate_email(cls, email):
        pattern = r"[\w.-]+@[\w-]+\.[\w.]+"
        match = re.match(pattern, email)
        if not match:
            raise ValueError('Email doesnt follow proper email format')
        return email
    
    @validator('gender')
    def validate_gender(cls, gender):
        allowed = ['male', 'female', 'other']
        if gender not in allowed:
            raise ValueError('Gender not allowed')
        return gender
    
    @validator('phone')
    def validate_phone(cls, phone):
        if len(phone) != 10:
            raise ValueError('Phone no. lemgth should be 10')
        return phone
        
    
    
    

try:
    valid = UserProfile(**user)
    if valid:
        print(valid)

except ValidationError as e:
    print(e)