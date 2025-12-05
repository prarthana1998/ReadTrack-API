from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table = True):
    id: Optional[int] = Field(default=None , primary_key= True)
    email : str
    password_hash : str

class Book(SQLModel, table = True):
    id: Optional[int] = Field(default=None , primary_key= True)
    user_id: int = Field(foreign_key = "user.id")
    name: str
    author: str
    genre : Optional[str] = None
