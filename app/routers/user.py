from fastapi import APIRouter, status
from sql.schemas.user import User
from sqlalchemy.orm import Session

from sql import models
from sql.schemas import user

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        404: {"description": "Not found"},
        401: {"description": "Unauthorized"},
    },
)


@router.post("/", status_code=status.HTTP_200_OK)
async def createUser(acount:User)->User:

    return {"message": "Hello World"}
