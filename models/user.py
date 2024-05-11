from pydantic import BaseModel
from pydantic import EmailStr

class UserIn(BaseModel):
  username: str
  password: str
  email: EmailStr
  full_name: str | None = None
