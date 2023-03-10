"""The entrypoint of the project"""
from fastapi import FastAPI
from todo import todo_router


app = FastAPI()


@app.get("/")
async def dummy_endpoint() -> dict:
    """The dummy root endpoint

    Returns:
        dict: The returned object
    """
    return {"Hello": "Good Morning"}

app.include_router(todo_router)
