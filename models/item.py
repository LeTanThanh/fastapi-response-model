from pydantic import BaseModel
from pydantic import Field

class Item(BaseModel):
  name: str = Field()
  description: str | None = Field(default = None)
  price: float = Field()
  tax: float | None = Field(default = None)
  tags: list[str] = Field(default = [])
