"""Created the model python script"""
from pydantic import BaseModel


class Todo(BaseModel):
    """The template for the Todo data

    Args:
        BaseModel (Parent class): The class which is inherited by Todo
    """
    id: int
    item: str
