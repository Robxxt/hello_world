from pydantic import BaseModel, ValidationError

def print_description(description: str):
    size = len(description)
    print(f"{'-' * (size + 4)}")
    print(f"| {description} |")
    print(f"{'-' * (size + 4)}")

def handle_model(model: type[BaseModel], **kwargs):
    """
    Initializes a model and display it's values.
    Otherwise raises an exception and displays it
    """
    try:
        model_init = model(**kwargs)
        print(model_init)
    except ValidationError as e:
        print(e)