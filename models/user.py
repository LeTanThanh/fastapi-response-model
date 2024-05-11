from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class UserIn(BaseModel):
  username: str = Field(examples = ["USER"])
  password: str = Field(examples = ["Aa@123456"])
  email: EmailStr = Field(examples = ["user@example.com"])
  full_name: str | None = Field(default = None, examples = ["USER"])

class UserOut(BaseModel):
  username: str = Field(examples = ["USER"])
  email: EmailStr = Field(examples = ["user@example.com"])
  full_name: str | None = Field(default = None, examples = ["USER"])
