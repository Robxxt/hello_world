from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    EmailStr,
    HttpUrl
)
from ipaddress import IPv4Address
from helpers_functions import print_description
from faker import Faker
import random

"""
For more info about Types check pydantic's documentation:
https://docs.pydantic.dev/latest/concepts/types/
"""

random.seed(42)

class Person(BaseModel):
    name: str = Field(max_length=20, min_length=2)
    age: PositiveInt
    email: EmailStr
    website: HttpUrl
    ipv4: IPv4Address

fake = Faker()

# Generate a list of 10 people with valid information
valid_employees = [
     {
        "name": fake.name(),
        "age": random.randint(0, 40),
        "ipv4": fake.ipv4(),
        "email": fake.email(),
        "website": fake.url(),
        "something_else": "not relevant"
     }
     for _ in range(10)
]

print_description("Display employee information without pydantic")
print(valid_employees)

employees: list[Person] = [Person(**employee) for employee in valid_employees]
print_description("Display employee information with pydantic")
print(employees)