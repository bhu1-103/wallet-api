from sqlalchemy.orm import Session
from models import User, Transaction

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_wallet(db: Session, user_id: int, amount: float):
    user = get_user(db, user_id)
    if not user:
        return None
    user.wallet_balance += amount
    transaction = Transaction(user_id=user_id, amount=amount)
    db.add(transaction)
    db.commit()
    db.refresh(user)
    db.refresh(transaction)
    return user

def get_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()
