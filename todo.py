"""The Todo route"""
from fastapi import APIRouter, Path
from model import Todo


todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    """Dumb endpoint for adding todos

    Args:
        todo (dict): The todo data structure

    Returns:
        dict: The data structure of the returned value
    """
    todo_list.append(todo)
    return {"Message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    """A dummy endpoints for fetching todos

    Returns:
        dict: The returned data structure
    """
    return {"Todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The id of the todo to retrieve")) -> dict:
    """An endpoint for getting a single todo

    Args:
        todo_id (int, optional): The id of the todo.
                                Defaults to Path(..., title="The id of the todo to retrieve").

    Returns:
        dict: The return value
    """
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
