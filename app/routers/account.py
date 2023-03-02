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
async def checkBalance(id, db: Session = Depends(get_db))->list[Account]:
    return db.query(models.Account).filter(models.Account.user_id == id).all()


@router.post("/consign", status_code=status.HTTP_200_OK)
async def consign(val:float, account_id:int, user_id: int, db: Session = Depends(get_db))->Account:
    p = db.query(models.Account).filter(models.Account.id == account_id ,models.Account.id == user_id)
    p.update({'amount':models.Account.amount + val },synchronize_session=False)
    db.commit()
    res = db.query(models.Account).filter(models.Account.id == account_id ,models.Account.id == user_id).first()
    return res

@router.post("/withdrawals", status_code=status.HTTP_200_OK)
async def withdrawals(val:float, account_id:int, user_id: int, db: Session = Depends(get_db)):
    p = db.query(models.Account).filter(models.Account.id == account_id ,models.Account.id == user_id)
    amount = p.first().amount
    if p :
        amount = p.first().amount >= val
        if amount:
            savings = p.filter(models.Account.amount >= val)
            savings.update({'amount':models.Account.amount + val },synchronize_session=False)
            db.commit()
        else:
            return {'fail': 'there is not enough savings'}

    res = db.query(models.Account).filter(models.Account.id == account_id ,models.Account.id == user_id).first()
    return res
