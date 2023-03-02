from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    #account = relationship("Account", back_populates="owner")


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String, default= None)
    amount = Column(Float,default= None)
    user_id = Column(Integer, ForeignKey("user.id"),)
    #account_id = relationship("User", back_populates="account")