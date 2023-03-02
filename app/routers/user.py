from fastapi import APIRouter, status, Depends, FastAPI, HTTPException
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
    prefix="/user",
    tags=["user"],
    responses={
        404: {"description": "Not found"},
        401: {"description": "Unauthorized"},
    },
)


@router.post("/", status_code=status.HTTP_200_OK)
async def createUser(user:User,  db: Session = Depends(get_db))->User:
    acc = models.User(**user.dict())
    db.add(acc)
    db.commit()
    db.refresh(acc)
    return {**user.dict()}



@router.get("/", status_code=status.HTTP_200_OK)
async def getUser(user_id:int,  db: Session = Depends(get_db))->User:
    return db.query(models.User).filter(models.User.id == user_id).first()


