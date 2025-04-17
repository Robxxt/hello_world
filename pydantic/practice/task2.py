"""
This task may require quite some effort.
- Create a pydantic model called Pokemon that contains:
    - id (integer, must be > 0)
    - name (string, length > 0 and < 12)
    - url (must be a valid url format)
    - base_experience (integer > 0)
    - height (integer > 0)
    - weight (integer > 0)
- You will need to get the first 12 pokemons from the list,
parse them into the Pokemon model and save them in a json file locally.

