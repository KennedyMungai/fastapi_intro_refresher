"""The Todo route"""
from fastapi import APIRouter
from model import Todo


todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
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
