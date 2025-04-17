from pydantic import BaseModel, ValidationError, Field
from helpers_functions import print_description

class Person(BaseModel):
    name: str = Field(max_length=20, min_length=2)
    # gt stands for greater than
    age: int = Field(ge=0)

print_description("Trying to initialize a model with invalid Field: name length < 2")
try:
    person_1 = Person(name="R", age=22)
except ValidationError as e:
    print(e)

print_description("Trying to initialize a model with invalid Field: age < 0")
try:
    person_1 = Person(name="Random", age=-1)
except ValidationError as e:
    print(e)

print_description("Initialize a valid model")
try:
    person_1 = Person(name="Random", age=22)
    print(person_1)
except ValidationError as e:
    print(e)