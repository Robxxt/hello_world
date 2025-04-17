from pydantic import BaseModel, Field
from helpers_functions import (
    print_description,
    handle_model
)
from faker import Faker
from case_4_apply_validators import User
import json
import os

fake = Faker()

class UserExpanded(User):
    irrelevant_info: str = Field(alias="irrelevant info")
    email: str = Field(alias="user email")

if __name__ == "__main__":
    user_list_information = [
        {
        "name": fake.name(),
        "password": fake.password(),
        "irrelevant info": fake.text(),
        "user email": fake.email(),
        }
        for _ in range(1000)
    ]

    if not os.path.isdir('data'):
        os.mkdir('data')
    # write the row data
    with open ("data/dirty_dictionary.json", 'w') as f:
        json.dump(user_list_information, f, indent=4)

    print_description("User information before being passed to User model: First Item")
    print(user_list_information[0])
    print_description("Converting to pydantic User object")
    pydantic_user_list = []
    for user_info in user_list_information:
        pydantic_user_list.append(UserExpanded(**user_info))
    print(pydantic_user_list[0])

    # write the pydantic data to json file
    with open ("data/clean_dictionary.json", 'w') as f:
        print_description("Writing a pre-processed json file")
        clean_list = [
            user_info.model_dump()
            for user_info in pydantic_user_list
        ]
        json.dump(clean_list, f, indent=4)
