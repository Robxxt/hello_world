from pydantic import BaseModel
import requests

class User(BaseModel):
    username: str
    email: str
    website: str

BASE_URL = "https://jsonplaceholder.typicode.com/users"
unprocessed_users_list = requests.get(BASE_URL).json()
processed_users_list = [User(**user_info) for user_info in unprocessed_users_list]

print(processed_users_list[:3])