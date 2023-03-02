from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    account_id: int

    class Config:
        orm_mode = True