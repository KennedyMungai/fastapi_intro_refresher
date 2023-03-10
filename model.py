"""Created the model python script"""
from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    """The template for the Todo data

    Args:
        BaseModel (Parent class): The class which is inherited by Todo
    """
    id: int
    item: str

    class Config:
        """Configuration for the Todo class"""
        schema_extra = {
            "Example": {
                "id": 1,
                "item": "Example Schema"
            }
        }


class TodoItem(BaseModel):
    """The template for the todo item

    Args:
        BaseModel (Class): The parent class of teh TodoItem
    """
    item: str

    class Config:
        """Config class for TodoItem"""
        schema_extra = {
            "example": {
                "item": "Bailando"
            }
        }


class TodoItems(BaseModel):
    """Defined the TodoItems class

    Args:
        BaseModel (Class): The parent class for the TodoItems
    """
    todos: List[TodoItem]

    class Config:
        """The config class for the TodoItems class
        """
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example Schema 1"
                    },
                    {
                        "item": "Example Schema 2"
                    }
                ]
            }
        }
