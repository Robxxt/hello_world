from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    name: str
    age: int

person_1 = Person(name="Robert", age=22)
print(person_1)

print("Trying to initialize a model with invalid age type")
try:
    person_1 = Person(name="Robert", age="hola")
except ValidationError as e:
    print(e)