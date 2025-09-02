from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    phone: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    wallet_balance: float

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float

class Transaction(TransactionBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class WalletUpdate(BaseModel):
    user_id: int
    amount: float
