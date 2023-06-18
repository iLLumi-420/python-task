from pydantic import BaseModel, ValidationError

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

try:
    user = {
        'name': 'Sandeep',
        'age': 'abc',
        'email': 'sandeep@gmail.com'
    }
    valid = UserProfile(**user)
    print(valid)

except ValidationError as e:
    print(e)