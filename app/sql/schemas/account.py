from typing import Union
from pydantic import BaseModel


class Account(BaseModel):
    id: int
    description: Union[str, None] = None
    amunt: float = None
    account_id : int

    class Config:
        orm_mode = True