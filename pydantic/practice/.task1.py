from pydantic import BaseModel
import requests
import sys

class User(BaseModel):
    username: str
    email: str
    website: str

"""
Please note that the BASE_URL shouldn't be visible like in this case.
Normally you would take it from the environment variables or a .env file
"""
BASE_URL = "https://jsonplaceholder.typicode.com/users12"
try:
    response = requests.get(BASE_URL)
    if not response.ok:
        raise ValueError(f"{response.status_code=}")
    unprocessed_users_list = response.json()
    processed_users_list = [User(**user_info) for user_info in unprocessed_users_list]
    print(processed_users_list[:3])
except Exception as e:
    sys.exit(f"Failed to establish connection with {BASE_URL}\n{e}")