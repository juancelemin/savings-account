from typing import Union
from pydantic import BaseModel


class Account(BaseModel):
    id: int
    description: Union[str, None] = 'Saving Account'
    amount: float = None
    user_id: int


    class Config:
        orm_mode = True