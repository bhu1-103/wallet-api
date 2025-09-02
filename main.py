from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, Base
import models, crud, schemas

Base.metadata.create_all(bind=engine)

#app = FastAPI(title="wallet-api")

app = FastAPI(
    title="wallet-api",
    description="API for managing user wallets and transactions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model=List[schemas.User])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/wallet/update/", response_model=schemas.User)
def update_wallet(wallet: schemas.WalletUpdate, db: Session = Depends(get_db)):
    user = crud.update_wallet(db, wallet.user_id, wallet.amount)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/transactions/{user_id}", response_model=List[schemas.Transaction])
def fetch_transactions(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_transactions(db, user_id)
