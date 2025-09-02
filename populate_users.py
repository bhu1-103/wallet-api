from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models

# Create tables if not already created
Base.metadata.create_all(bind=engine)

# Sample users
sample_users = [
    {"name": "bhu1", "email": "bhu1@protonmail.com", "phone": "1234567890"},
    {"name": "bhu2", "email": "bhu2@outlook.com", "phone": "1357924680"},
    {"name": "bhu3", "email": "bhu3@yahoo.com", "phone": "369258147"},
    {"name": "bhu4", "email": "bhu4@hotmail.com", "phone": "321654987"},
    {"name": "bhu5", "email": "bhu5@gmail.com", "phone": "6942069420"},
]

def populate_users():
    db: Session = SessionLocal()
    for user_data in sample_users:
        user = models.User(
            name=user_data["name"],
            email=user_data["email"],
            phone=user_data["phone"],
            wallet_balance=0.0
        )
        db.add(user)
    db.commit()
    db.close()
    print("Sample users added")

if __name__ == "__main__":
    populate_users()
