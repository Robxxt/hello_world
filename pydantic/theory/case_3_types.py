from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    EmailStr,
    HttpUrl
)
from ipaddress import IPv4Address
from helpers_functions import (
    print_description,
    handle_model
)
from faker import Faker
import random

"""
For more info about Types check pydantic's documentation:
https://docs.pydantic.dev/latest/concepts/types/
"""

class Person(BaseModel):
    name: str = Field(max_length=40, min_length=2)
    age: PositiveInt
    email: EmailStr
    website: HttpUrl
    ipv4: IPv4Address

if __name__ == "__main__":
    random.seed(42)

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

    print_description("Example with invalid ip address and website")
    person_data = {
            "name": fake.name(),
            "age": random.randint(1, 40),
            "ipv4": "1902.168.1.1",
            "email": fake.email(),
            "website": "example",
            "something_else": "not relevant"
    }
    handle_model(Person, **person_data)