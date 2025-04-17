from pydantic import BaseModel, field_validator
from helpers_functions import (
    print_description,
    handle_model
)
from faker import Faker
import hashlib

fake = Faker()

class User(BaseModel):
    name: str
    password: str

    @field_validator('name')
    def title_name(cls, value):
        return value.title()

    @field_validator('password')
    def hash_password(cls, value):
        hash_object = hashlib.sha256()
        hash_object.update(value.encode('utf-8'))
        hashed_string = hash_object.hexdigest()
        return hashed_string

if __name__ == "__main__":
    user_info = {
        "name": fake.name(),
        "password": fake.password()
    }
    print_description("User information before being passed to User model")
    print(user_info)
    print_description("Final look of User model")
    handle_model(User, **user_info)