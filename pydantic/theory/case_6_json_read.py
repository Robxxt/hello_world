from case_5_json_write import UserExpanded
import json
import os, sys
from helpers_functions import print_description

if not os.path.isdir('data'):
    sys.exit(
    "Missing data folder.\n\
    Please make sure to first generate the data running:\n\
    python3 case_5_json_write.py"
    )

# read the dirty json json file
with open("data/dirty_dictionary.json", 'r') as f:
    user_list = json.load(f)

print_description("Fist user from json file")
print(user_list[0])

user_processed_list = [UserExpanded(**user) for user in user_list]
print_description("Fist user from pydantic list")
print(user_processed_list[0])