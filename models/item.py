from pydantic import BaseModel
from pydantic import Field

class Item(BaseModel):
  name: str = Field()
  description: str | None = Field(default = None)
  price: float = Field(default = 10.5)
  tax: float | None = Field(default = None)
  tags: list[str] = Field(default = [])
