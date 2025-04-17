from pydantic import BaseModel, ValidationError
from helpers_functions import print_description

class Person(BaseModel):
    name: str
    age: int

person_1 = Person(name="Random", age=22)
print(person_1)

print_description("Trying to initialize a model with invalid age type")
try:
    person_1 = Person(name="Random", age="hola")
except ValidationError as e:
    print(e)

print_description("Initialize a valid model")
try:
    person_1 = Person(name="Random", age="hola")
    print(person_1)
except ValidationError as e:
    print(e)