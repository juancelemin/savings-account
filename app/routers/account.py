from fastapi import APIRouter, status, Depends, FastAPI, HTTPException
from sql.schemas.account import Account
from sql.schemas.user import User
from sqlalchemy.orm import Session

from sql import models
from sql.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={
        404: {"description": "Not found"},
        401: {"description": "Unauthorized"},
    },
)


@router.post("/", status_code=status.HTTP_200_OK)
async def account(account:Account, db: Session = Depends(get_db)):
    acc = models.Account(**account.dict())
    db.add(acc)
    db.commit()
    db.refresh(acc)
    return {**account.dict()}


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
