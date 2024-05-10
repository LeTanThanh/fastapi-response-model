from fastapi import FastAPI
from fastapi import Body

from typing import Annotated

from models.item import Item

app = FastAPI()

@app.post("/items")
async def create_item(item: Annotated[Item, Body(embed = True)]) -> Item:
  return item

@app.get("/items")
async def read_items() -> list[Item]:
  return [
    Item(name = "Portal Gun", price=42.0),
    Item(name = "Plumbus", price=32.0)
  ]
