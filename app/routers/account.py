from fastapi import APIRouter, status
from sql.schemas.account import Account
from sqlalchemy.orm import Session

from sql import models
from sql.schemas import account

router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={
        404: {"description": "Not found"},
        401: {"description": "Unauthorized"},
    },
)


@router.post("/", status_code=status.HTTP_200_OK)
async def account(acount:Account)->Account:
    """

    """
    return {"message": "Hello World"}


@router.get("/check/{id}", status_code=status.HTTP_200_OK)
async def checkBalance()->Account:
    """

    """
    return {"message": id}


@router.post("/consign", status_code=status.HTTP_200_OK)
async def consign(val:float)->Account:
    """

    """
    return {"message": val}


@router.post("/withdrawals", status_code=status.HTTP_200_OK)
async def withdrawals(val:float)-> Account:
    """

    """
    return {"message": val}
