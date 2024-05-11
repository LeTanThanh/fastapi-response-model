from fastapi import FastAPI
from fastapi import Body

from typing import Annotated
from typing import Any

from models.item import Item
from models.user import UserIn
from models.user import UserOut

app = FastAPI()

# Response Model - Return Type
"""
@app.post("/items")
async def create_item(item: Annotated[Item, Body(embed = True)]) -> Item:
  return item

@app.get("/items")
async def read_items() -> list[Item]:
  return [
    Item(name = "Portal Gun", price=42.0),
    Item(name = "Plumbus", price=32.0)
  ]
"""

# response_model Parameter
@app.post("/items", response_model = Item)
async def create_item(item: Annotated[Item, Body()]) -> Any:
  return item

@app.get("/items", response_model=list[Item])
async def read_items() -> Any:
  return [
    Item(name = "Portal Gun", price=42.0),
    Item(name = "Plumbus", price=32.0)
  ]

# Return the same input data
"""
@app.post("/users", response_model = UserIn)
async def create_users(user: Annotated[UserIn, Body(embed = True)]):
  return user
"""

# Add an output model
@app.post("/users", response_model = UserOut)
async def create_user(user: Annotated[UserIn, Body(embed = True)]):
  return user

# response_model or Return Type

"""
In this case, because the two models are different, if we annotated the function return type as UserOut, the editor and tools would complain that we are returning an invalid type, as those are different classes.

That's why in this example we have to declare it in the response_model parameter.

... but continue reading below to see how to overcome that.
"""
