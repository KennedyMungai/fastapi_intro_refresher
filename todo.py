"""The Todo route"""
from fastapi import APIRouter, Path
from model import Todo, TodoItem


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


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    """An API endpoint to update Todo entries

    Args:
        todo_data (int): The data to update the item
        todo_id (int, optional): _description_. Defaults to Path(..., title="The ID of the todo to be updated").

    Returns:
        dict: A message to show success
    """
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item

            return {
                "Message": "Todo updated successfully"
            }

    return {
        "Message": "Todo with supplied Id doesn't exist"
    }


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    """The delete Todo endpoint

    Args:
        todo_id (int): The id of the todo

    Returns:
        dict: A message
    """
    for index in range(len(todo_list)):
        todo == todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            todo_list.pop(index)

            return {
                "Message": "Todo deleted successfully"
            }

    return {
        "Message": "Todo deleted successfully"
    }
